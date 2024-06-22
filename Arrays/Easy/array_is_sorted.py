# Check if an array is sorted

def check_array_is_sorted(arr: list) -> bool:
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
        
    return True

print(check_array_is_sorted([2,5,1,3,0,-1,-25]))
print(check_array_is_sorted([1,2,3,4,5]))

# Time complexity: O(n)
# Space complexity: O(1)
