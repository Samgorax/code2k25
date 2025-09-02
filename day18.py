def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1  # perfect square case
            else:
                count += 2  # i and n//i both are divisors
        i += 1
    return count

# -------- Testing --------
print("Divisors of 12:", count_divisors(12))   # 6 (1,2,3,4,6,12)
print("Divisors of 36:", count_divisors(36))   # 9 (1,2,3,4,6,9,12,18,36)
print("Divisors of 97:", count_divisors(97))   # 2 (1,97 - since prime)
