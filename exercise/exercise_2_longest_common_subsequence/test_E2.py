from exercise_2_longest_common_subsequence import *
import unittest

class TestLCM(unittest.TestCase):

    def test_short_0(self):
        seq1 = "A"
        seq2 = "B"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 0)
    def test_short_1(self):
        seq1 = "A"
        seq2 = "A"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 1)
    def test_middle_of_sequences(self):
        seq1 = "ABCA"
        seq2 = "BBCB"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 2)
    def test_start_of_sequences(self):
        seq1 = "ABDD"
        seq2 = "ABEE"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 2)
    def test_end_of_sequences(self):
        seq1 = "AABC"
        seq2 = "GGBC"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 2)
    def test_cross_match(self):
        seq1 = "AABC"
        seq2 = "BCGG"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 2)
    def test_find_longer1(self):
        seq1 = "AABCAAAEFEA"
        seq2 = "VVEFEVVVBCV"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 3)
    def test_remove_from_between(self):
        seq1 = "AABCCAAAEFA"
        seq2 = "VVBCCVVVEFV"
        self.assertEqual(longest_common_subsequence(seq1, seq2), 5)

unittest.main()
