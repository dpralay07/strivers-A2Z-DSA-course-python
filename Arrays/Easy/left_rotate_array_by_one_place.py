# Left rotate an array by one place

def left_rotate(arr:list) -> list:
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = temp

    return arr

print(left_rotate([2,5,1,3,0,-1,-25]))

# Time complexity: O(n)
# Space complexity: O(1)