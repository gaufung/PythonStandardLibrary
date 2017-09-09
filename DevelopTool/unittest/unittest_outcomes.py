import unittest

class OutcomeTest(unittest.TestCase):
    def testPass(self):
        return
    def testFail(self):
        self.assertFalse(True)
    def testError(self):
        raise RuntimeError('Test error!')