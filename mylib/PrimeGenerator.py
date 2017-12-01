# Generate all primes up to n
def generate_primes(n):
    is_prime = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i+i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]

# check if number if prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# test
print(generate_primes(100))
print(is_prime(515051))
