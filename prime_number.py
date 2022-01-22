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
    s=0
    for i in range(2,n):
        if is_prime(i):
            s+=1
    
    return s
print(prime_number(100))