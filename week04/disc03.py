def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if m >= n:
        if n == 1:
            return m
        else:
            return m + multiply(m, n-1)
    if m < n:
        if m == 1:
            return n
        else:
            return n + multiply(m-1, n)


def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)
    

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def prime_helper(n, i):
        if i == 1:
            return True
        elif n % i == 0:
            return False
        else:
            return prime_helper(n, i - 1)
    return prime_helper(n, n - 1)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
    

def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    # If one of the numbers is zero, return the other number.
    if not n1 or not n2:
        return n1 or n2

    # Convert numbers to strings for comparison and concatenation.
    s1, s2 = str(n1), str(n2)

    # Choose the number with the higher leading digit or the higher value if equal length.
    if s1[0] > s2[0] or (s1[0] == s2[0] and n1 >= n2):
        return int(s1[0] + str(merge(int(s1[1:]) if len(s1) > 1 else 0, n2)))
    else:
        return int(s2[0] + str(merge(n1, int(s2[1:]) if len(s2) > 1 else 0)))



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('All tests passed!')
