def findLeaders(arr):
    n = len(arr)
    leaders = []
    
    # last element is always a leader
    maxRight = arr[-1]
    leaders.append(maxRight)
    
    # traverse from right to left
    for i in range(n-2, -1, -1):
        if arr[i] >= maxRight:
            leaders.append(arr[i])
            maxRight = arr[i]
    
    # reverse to keep original order
    leaders.reverse()
    return leaders


# ---------- test ----------
print("Test 1:", findLeaders([16, 17, 4, 3, 5, 2]))   # [17, 5, 2]
print("Test 2:", findLeaders([1, 2, 3, 4, 0]))        # [4, 0]
print("Test 3:", findLeaders([7, 10, 4, 6, 5, 2]))    # [10, 6, 5, 2]
print("Test 4:", findLeaders([5])) # [5]


Output:


Test 1: [17, 5, 2]
Test 2: [4, 0]
Test 3: [10, 6, 5, 2]
Test 4: [5]
