from is_prime import is_prime
from prime_number import prime_number

#Define function,Find list of prime numbers in a given range.
def prime_range(start:int, end:int)->list:
    """
    Find list of prime numbers in range.
    Parameters:
        start (int): start of range
        end (int): end of range
    Returns:
        list: list of prime numbers in range
    """
    a=[]
    for i in range(start,end):
        if is_prime(i):
            a.append(i)
            


    return a

#Test function.

print(prime_range(10,100))