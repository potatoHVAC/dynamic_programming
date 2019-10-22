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
