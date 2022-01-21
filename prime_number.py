from is_prime import is_prime
#Define function, Find the number of prime numbers which are less than n.

def prime_number(n:int)->int:
    """
    Find the number of prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        int: Number of prime numbers
    """
    count = 0
    for i in range(1, n):
        if is_prime(i):
            print(i)
            count += 1
    return count
print(prime_number(10))