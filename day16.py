def gcd(a, b):
    # Euclid's algorithm
    while b != 0:
        a, b = b, a % b
    return a

def lcm(n, m):
    # n, m >= 1 as per problem
    g = gcd(n, m)
    # order like this to avoid big intermediate (though Python is safe)
    return (n // g) * m

# -------- testing --------
print("LCM(4, 6)  =", lcm(4, 6))     # 12
print("LCM(21, 6) =", lcm(21, 6))    # 42
print("LCM(1, 10) =", lcm(1, 10))    # 10
print("LCM(1000000000, 2) =", lcm(10**9, 2))  # 1000000000
