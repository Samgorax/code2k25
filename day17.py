def prime_factorization(n):
    factors = []
    
    # factor 2 ko alag handle karo (even numbers)
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # ab odd factors check karenge 3,5,7... sqrt(n)
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2  # sirf odd hi check karna hai

    # agar abhi bhi n > 1 bacha hai toh woh prime hai
    if n > 1:
        factors.append(n)
    
    return factors

# -------- Testing --------
print("Prime factors of 18:", prime_factorization(18))   # [2, 3, 3]
print("Prime factors of 97:", prime_factorization(97))   # [97] (prime)
print("Prime factors of 100:", prime_factorization(100)) # [2, 2, 5, 5]
