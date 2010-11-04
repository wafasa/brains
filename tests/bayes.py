import unittest

import brains

class BayesTestCase(unittest.TestCase):

    def test_classify(s):
        f = brains.DataFile("data/mushroom.csv")
        b = brains.Bayes(f.features)
        test, train = f.split(4)
        for p in train:
            b.train(p[0], p[1])
        correct = 0.0
        for t in test:
            predict = b.classify(t[1])
            if t[0] == predict:
                correct += 1
        s.assertGreater(correct / len(test), 0.9)



        