# Find largest element in an array

def find_largest_element(arr: list) -> int:
    largest_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest_element:
            largest_element = arr[i]
    
    return largest_element

print(find_largest_element([2,5,1,3,0,-1,-25]))

# Time complexity: O(n)
# Space complexity: O(1)
