import csv, util, solver, baseline, string
from itertools import izip

def score_accuracy(original_text, key, guess_text, guess_key):
    return sum([1 for i in xrange(len(key.strip())) if key[i] == guess_key[i]])/float(26)

def main():
    verbose = False
    keys_file = open("keys", 'r')
    cipher_text_file = open("substitute", 'r') # or open("substitute_noise", 'r')
    original_text_file = open("original", "r")

    cipher_solver = solver.Solver()
    cipher_baseline = baseline.Baseline()
    solver_accuracy = []
    baseline_accuracy = []

    for original_text, key, cipher_text in izip(original_text_file, keys_file, cipher_text_file):
        if verbose:
            print "Original Text", original_text
            print "Cipher Text", cipher_text
        
        # original_text = "The arsenal suggested a level of planning that added to investigators' concern that Wednesday's shootings, which left 14 dead and 21 injured"
        # key = util.generateKey()
        # cipher_text = util.encrypt(original_text, key)
        baseline_text, baseline_key = cipher_baseline.decrypt(cipher_text)
        baseline_accuracy = score_accuracy(original_text, key, baseline_text, baseline_key)
        guess_text, guess_key = cipher_solver.decrypt(cipher_text)
        accuracy = score_accuracy(original_text, key, guess_text, guess_key)
        solver_accuracy.append(accuracy)

    print "Average Accuracy of Baseline: ", sum(baseline_accuracy)/len(baseline_accuracy)
    print "Average Accuracy of Solver: ", sum(solver_accuracy)/len(solver_accuracy)
    print "Over %d cipher texts" % len(solver_accuracy)

if __name__ == '__main__':
    main()
