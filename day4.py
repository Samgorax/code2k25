import math

def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)
    gap = math.ceil((m+n)/2)

    while gap > 0:
        i = 0
        j = gap
        while j < (m+n):
            # find actual elements from arr1/arr2
            if i < m:
                a = arr1[i]
            else:
                a = arr2[i-m]
            
            if j < m:
                b = arr1[j]
            else:
                b = arr2[j-m]
            
            # swap if needed
            if a > b:
                if i < m and j < m:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < m and j >= m:
                    arr1[i], arr2[j-m] = arr2[j-m], arr1[i]
                else:
                    arr2[i-m], arr2[j-m] = arr2[j-m], arr2[i-m]
            
            i += 1
            j += 1
        
        if gap == 1:
            break
        gap = math.ceil(gap/2)


# ------------ test ----------
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print("Before:")
print("arr1:", arr1)
print("arr2:", arr2)

merge(arr1, arr2)

print("After:")
print("arr1:", arr1)
print("arr2:", arr2)





Outputs:

Before:
arr1: [1, 3, 5, 7]
arr2: [2, 4, 6, 8]

After:
arr1: [1, 2, 3, 4]
arr2: [5, 6, 7, 8]
