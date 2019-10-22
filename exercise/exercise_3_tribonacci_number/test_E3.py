from exercise_3_tribonacci import *
import unittest

class TestFibonacci(unittest.TestCase):

    def test_1st_tribonacci(self):
        self.assertEqual(tribonacci(0), 0)
    def test_2nd_tribonacci(self):
        self.assertEqual(tribonacci(1), 1)
    def test_3rd_tribonacci(self):
        self.assertEqual(tribonacci(2), 1)
    def test_4th_tribonacci(self):
        self.assertEqual(tribonacci(3), 2)
    def test_5th_tribonacci(self):
        self.assertEqual(tribonacci(4), 4)
    def test_25th_tribonacci(self):
        self.assertEqual(tribonacci(25), 1389537)
        
unittest.main()
