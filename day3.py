def findDuplicate(arr):
    # Phase 1: detect cycle (tortoise and hare)
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]       # move 1 step
        fast = arr[arr[fast]]  # move 2 steps
        if slow == fast:
            break
    
    # Phase 2: find entry point (duplicate number)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow


# ---------- testing ----------
print("Test 1:", findDuplicate([3, 1, 3, 4, 2]))   # 3
print("Test 2:", findDuplicate([1, 3, 4, 2, 2]))   # 2
print("Test 3:", findDuplicate([1, 1]))            # 1
print("Test 4:", findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1])) # 9
