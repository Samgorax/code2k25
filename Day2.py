def missingNumber(arr):
    n = len(arr) + 1   # because ek number missing hai
    
    # Step 1: XOR of 1 to n
    total_xor = 0
    for i in range(1, n+1):
        total_xor ^= i
    
    # Step 2: XOR of all elements of array
    arr_xor = 0
    for num in arr:
        arr_xor ^= num
    
    # Step 3: missing number = xor of both
    return total_xor ^ arr_xor


# ---------- testing ----------
print("Test 1:", missingNumber([1, 2, 4, 5]))   # 3
print("Test 2:", missingNumber([2, 3, 4, 5]))   # 1
print("Test 3:", missingNumber([1, 2, 3, 4]))   # 5
print("Test 4:", missingNumber([1]))            # 2
