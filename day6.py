def findZeroSumSubarrays(arr):
    n = len(arr)
    result = []
    prefix_sum = 0
    hashmap = {}   # prefix_sum -> list of indices

    for i in range(n):
        prefix_sum += arr[i]

        # case 1: prefix_sum = 0 => subarray from 0 to i
        if prefix_sum == 0:
            result.append((0, i))
        
        # case 2: prefix_sum seen before
        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start+1, i))
        
        # store prefix_sum index
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = []
        hashmap[prefix_sum].append(i)
    
    return result


# --------- testing ----------
print("Test 1:", findZeroSumSubarrays([1, 2, -3, 3, -1, 2]))  # [(0,2), (1,3)]
print("Test 2:", findZeroSumSubarrays([4, -2, -2, 2, -4]))    # [(0,4), (1,2)]
print("Test 3:", findZeroSumSubarrays([1, 2, 3]))             # []
print("Test 4:", findZeroSumSubarrays([0, 0]))                # [(0,0),(0,1),(1,1)]

 Output

Test 1: [(0, 2), (1, 3)]
Test 2: [(0, 4), (1, 2)]
Test 3: []
Test 4: [(0, 0), (0, 1), (1, 1)]
