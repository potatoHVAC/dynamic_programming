#-------------------------------------------------------------------------------
#   Nth value of the Fibonacci Sequence
#-------------------------------------------------------------------------------

def main(n: int):
    """Return list with counts of each time an integer is evaluated"""
    
    count = [0 for _ in range(n)]
    memoize = {1: 0, 2: 1}
    
    def fibonacci(n: int) -> int:
        
        count[n-1] += 1
        if n not in memoize:
    
            memoize[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return memoize[n]

    fibonacci(n)
    return count

print(main(25))

    
