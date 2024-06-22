# Find second smallest element in an array
import sys
LARGEST_INTEGER = sys.maxsize


def find_second_smallest_element(arr: list) -> int:
    smallest_element = second_smallest_element = LARGEST_INTEGER
    for i in range(len(arr)):
        if arr[i] < smallest_element:
            second_smallest_element = smallest_element
            smallest_element = arr[i]
        elif arr[i] < second_smallest_element:
            second_smallest_element = arr[i]

    return second_smallest_element

print(find_second_smallest_element([2,5,1,3,0,-1,-25]))

# Time complexity: O(n)
# Space complexity: O(1)