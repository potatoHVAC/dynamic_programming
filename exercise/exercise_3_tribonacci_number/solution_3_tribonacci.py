#-------------------------------------------------------------------------------
#   Nth value of the Tribonacci Sequence
#-------------------------------------------------------------------------------

def tribonacci(n: int) -> int:
    """Find the nth term of the Tribonacci Sequence
    
    Input:
    :n: int -> target number
        
    Output: 
    int -> nth term of sequence
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

#-------------------------------------------------------------------------------
#   Create inner function
#-------------------------------------------------------------------------------

def tribonacci(n: int) -> int:

    def _tribonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
    
        return _tribonacci(n - 1) + _tribonacci(n - 2) + _tribonacci(n - 3)

    return _tribonacci(n)

#-------------------------------------------------------------------------------
#   Add Memoization
#-------------------------------------------------------------------------------

def tribonacci(n: int) -> int:

    memoize = {}
    def _tribonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        if n in memoize:
            return memoize[n]
        else:
            nth_tribonacci = _tribonacci(n - 1) + _tribonacci(n - 2) + _tribonacci(n - 3)
            memoize[n] = nth_tribonacci
            return memoize[n]

    return _tribonacci(n)

#-------------------------------------------------------------------------------
#   Move edge case into memoize
#-------------------------------------------------------------------------------

def tribonacci(n: int) -> int:

    memoize = {0: 0, 1: 1, 2: 1}
    def _tribonacci(n):
        if n in memoize:
            return memoize[n]
        else:
            nth_tribonacci = _tribonacci(n - 1) + _tribonacci(n - 2) + _tribonacci(n - 3)
            memoize[n] = nth_tribonacci
            return memoize[n]

    return _tribonacci(n)

#-------------------------------------------------------------------------------
#   Adhere to DRY coding practices
#-------------------------------------------------------------------------------

def tribonacci(n: int) -> int:

    memoize = {0: 0, 1: 1, 2: 1}
    def _tribonacci(n):
        if n not in memoize:
            memoize[n] = _tribonacci(n - 1) + _tribonacci(n - 2) + _tribonacci(n - 3)

        return memoize[n]

    return _tribonacci(n)
