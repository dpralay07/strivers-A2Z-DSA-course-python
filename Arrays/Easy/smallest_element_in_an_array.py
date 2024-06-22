# Find smallest element in an array

def find_smallest_element(arr: list) -> int:
    smallest_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
    
    return smallest_element

print(find_smallest_element([2,5,1,3,0,-1,-25]))

# Time complexity: O(n)
# Space complexity: O(1)
