#-------------------------------------------------------------------------------
#   Nth value of the Fibonacci Sequence
#-------------------------------------------------------------------------------

def main(n: int):
    """Return list with counts of each time an integer is evaluated"""
    
    count = [0 for _ in range(n)]
    def fibonacci(n: int) -> int:
        count[n-1] += 1
        if n == 1:
            return 0
        if n == 2:
            return 1
    
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(n)
    return count

print(main(25))

    
