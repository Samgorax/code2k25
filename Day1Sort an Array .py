def sort012(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    # using Dutch national flag method
    while mid <= high:
        if arr[mid] == 0:
            # swap with low
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # means arr[mid] == 2
            # swap with high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# test the function
a = [0,1,2,1,0,2,1,0]
print("before sort:", a)
sort012(a)
print("after sort :", a)


Sample output when you run it:

before sort: [0, 1, 2, 1, 0, 2, 1, 0]
after sort : [0, 0, 0, 1, 1, 1, 2, 2]
