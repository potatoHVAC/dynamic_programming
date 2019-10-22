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

#-------------------------------------------------------------------------------
#   Create memoize key generator
#-------------------------------------------------------------------------------
"""
  We need a unique key to be able to reference each possible step in the query.
Create a method for generating a key based on the input pointers. This will be 
a comma seperated string.

EX: 
pos1 = 3, pos2 = 5 
key = "3,5"
"""

def longest_common_subsequence(seq1: str, seq2: str) -> int:

    # Unique key generator
    def _memoize_key(pos1, pos2) -> str:
        """Return comma seperated string from two numbers"""
        return ",".join([str(pos1), str(pos2)])
        
    def _lcs(seq1, seq2, pos1, pos2) -> int:
        """Recursively find the longest common substring"""
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

#-------------------------------------------------------------------------------
#   Add memoize to recursive function
#-------------------------------------------------------------------------------
"""
* Add memoize dictionary.
* Generate memoize key.
* Check if result already exists.
* Replace recursive returns with variable assignments.
* Record result when found.
"""
def longest_common_subsequence(seq1: str, seq2: str) -> int:

    def _memoize_key(pos1, pos2) -> str:
        """Return comma seperated string from two numbers"""
        return ",".join([str(pos1), str(pos2)])

    # Add memoize
    memoize_lcs = {} 
    def _lcs(seq1, seq2, pos1, pos2) -> int:
        """Dynamically find the longest common substring"""
        if pos1 == -1 or pos2 == -1:
            return 0

        # Generate key based on positions
        lcs_key = _memoize_key(pos1, pos2) 

        # Check if result already exists
        if lcs_key not in memoize_lcs:
            if seq1[pos1] == seq2[pos2]:
                # Replace 'return' with variable assignment
                current_lcs = 1 + _lcs(seq1, seq2, pos1 - 1, pos2 - 1)
            else:
                # Replace 'return' with variable assignment                
                current_lcs = max(
                    _lcs(seq1, seq2, pos1, pos2 - 1),
                    _lcs(seq1, seq2, pos1 - 1, pos2)                
                )
            # Record the result
            memoize_lcs[lcs_key] = current_lcs

        return memoize_lcs[lcs_key]

    return _lcs(seq1, seq2, len(seq1) - 1, len(seq2) - 1)

#-------------------------------------------------------------------------------
#   Move edge cases into memoize
#-------------------------------------------------------------------------------
"""
  We need to catch all the end conditions. That could be accomplished by 
including all possible combinations of positions and -1 or by using the key
generator to catch all endings and use a common key.
"""

def longest_common_subsequence(seq1: str, seq2: str) -> int:

    def _memoize_key(pos1, pos2) -> str:
        """Return comma seperated string from two numbers"""
        # Capture all end conditions
        if pos1 == -1 or pos2 == -1:
            return "end"
        return ",".join([str(pos1), str(pos2)])

    # Update memoize edge case
    memoize_lcs = {"end": 0}
    def _lcs(seq1, seq2, pos1, pos2) -> int:
        """Dynamically find the longest common substring"""
        lcs_key = _memoize_key(pos1, pos2)

        if lcs_key not in memoize_lcs:
            if seq1[pos1] == seq2[pos2]:
                current_lcs = 1 + _lcs(seq1, seq2, pos1 - 1, pos2 - 1)
            else:
                current_lcs = max(
                    _lcs(seq1, seq2, pos1, pos2 - 1),
                    _lcs(seq1, seq2, pos1 - 1, pos2)                
                )
            memoize_lcs[lcs_key] = current_lcs

        return memoize_lcs[lcs_key]

    return _lcs(seq1, seq2, len(seq1) - 1, len(seq2) - 1)

