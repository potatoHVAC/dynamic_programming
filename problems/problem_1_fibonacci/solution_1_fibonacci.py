#-------------------------------------------------------------------------------
#   Nth value of the Fibonacci Sequence
#-------------------------------------------------------------------------------

def fibonacci(n: int) -> int:
    """Find the nth term of the Fibonacci Sequence
    
    Input:
    :n: int -> target number
        
    Output: 
    int -> nth term of sequence
    """

    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

#-------------------------------------------------------------------------------
#   Create inner function
#-------------------------------------------------------------------------------

def fibonacci(n: int) -> int:
    
    def _fibonacci(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
    
        return fibonacci(n - 1) + fibonacci(n - 2)

    return _fibonacci(n)

#-------------------------------------------------------------------------------
#   Add Memoization
#-------------------------------------------------------------------------------

def fibonacci(n: int) -> int:

    # Create Memoize
    memoize_fibonacci = {}
    def _fibonacci(n):
        if n == 1:
            return 0
        if n == 2:
            return 1

        # Check to see if value already exists
        if n in memoize_fibonacci:
            return memoize_fibonacci[n]
        else:
            nth_fibonacci =  fibonacci(n - 1) + fibonacci(n - 2)
            # Add value to memoize
            memoize_fibonacci[n] = nth_fibonacci
            return memoize_fibonacci[n]

    return _fibonacci(n)

#-------------------------------------------------------------------------------
#   Move edge case into memoize
#-------------------------------------------------------------------------------

def fibonacci(n: int) -> int:

    memoize_fibonacci = {1: 0, 2: 1}
    def _fibonacci(n):
        if n in memoize_fibonacci:
            return memoize_fibonacci[n]
        else:
            nth_fibonacci =  fibonacci(n - 1) + fibonacci(n - 2)
            memoize_fibonacci[n] = nth_fibonacci
            return memoize_fibonacci[n]

    return _fibonacci(n)

#-------------------------------------------------------------------------------
#   Adhere to DRY coding practices
#-------------------------------------------------------------------------------

def fibonacci(n: int) -> int:

    memoize_fibonacci = {1: 0, 2: 1}
    def _fibonacci(n):
        if n not in memoize_fibonacci:
            nth_fibonacci = fibonacci(n - 1) + fibonacci(n - 2)
            memoize_fibonacci[n] = nth_fibonacci
            
        return memoize_fibonacci[n]

    return _fibonacci(n)

