# Right rotate an array by k place

def right_rotate(arr:list, k:int) -> list:
    def reverse(nums:list, start:int, end:int) -> list:
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums

    n = len(arr)
    k = k % n

    arr = reverse(arr, n-k, n-1)
    arr = reverse(arr, 0, n-k-1)
    arr = reverse(arr, 0, n-1)
    return arr

print(right_rotate([2,5,1,3,0,-1,-25], 4))

# Time complexity: O(n)
# Space complexity: O(1)