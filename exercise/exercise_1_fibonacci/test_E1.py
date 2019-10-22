from exercise_1_fibonacci import *
import unittest

class TestFibonacci(unittest.TestCase):

    def test_1st_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
    def test_2nd_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
    def test_3rd_fibonacci(self):
        self.assertEqual(fibonacci(2), 1)
    def test_4th_fibonacci(self):
        self.assertEqual(fibonacci(3), 2)
    def test_5th_fibonacci(self):
        self.assertEqual(fibonacci(4), 3)
    def test_35th_fibonacci(self):
        self.assertEqual(fibonacci(34), 5702887)    

unittest.main()
