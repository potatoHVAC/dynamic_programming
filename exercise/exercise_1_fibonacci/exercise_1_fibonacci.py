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
