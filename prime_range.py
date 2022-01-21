from is_prime import is_prime

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
    prime_list = []
    for i in range(start, end+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

#Test function.
print(prime_range(1, 10))
print(prime_range(10, 20))