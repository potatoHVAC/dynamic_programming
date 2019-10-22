#-------------------------------------------------------------------------------
#   Longest Common Subsequence
#-------------------------------------------------------------------------------

def longest_common_subsequence(seq1: str, seq2: str) -> int:
    """Find the longest common subsequence of two strings

    Input:
    :seq1: str -> first sequence string
    :seq2: str -> second sequence string

    Output:
    int -> length of the longest common subsequence
    """

    def _lcs(seq1, seq2, pos1, pos2):
        if pos1 == -1 or pos2 == -1:
            return 0
        
        elif seq1[pos1] == seq2[pos2]:
            return 1 + _lcs(seq1, seq2, pos1 - 1, pos2 - 1)
        else:
            return max(
                _lcs(seq1, seq2, pos1, pos2 - 1),
                _lcs(seq1, seq2, pos1 - 1, pos2)                
            )

    return _lcs(seq1, seq2, len(seq1) - 1, len(seq2) - 1)

