def trap(height):
    n = len(height)
    if n == 0:
        return 0
    
    left, right = 0, n-1
    leftMax, rightMax = 0, 0
    water = 0
    
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1
    
    return water


# -------- testing --------
print("Test 1:", trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print("Test 2:", trap([4,2,0,3,2,5]))              # 9
print("Test 3:", trap([1,2,3,4]))                  # 0
print("Test 4:", trap([5,4,1,2]))                  # 1


 Output:

Test 1: 6
Test 2: 9
Test 3: 0
Test 4: 1
