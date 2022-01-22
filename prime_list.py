from is_prime import is_prime
#Define function, Find the all prime numbers which are less than n.
def prime_list(n:int)->list:
    """
    Find the all prime numbers which are less than n.
    Parameters:
        n (int): Given number
    Returns:
        list: List of prime numbers
    """
    a=[]
    for i in range(2,n):
        if is_prime(i):
            a.append(i)
    
    return a
print(prime_list(100))

