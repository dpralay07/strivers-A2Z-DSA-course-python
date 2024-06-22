# Find second largest element in an array
import sys
SMALLEST_INTEGER = -sys.maxsize-1


def find_second_largest_element(arr: list) -> int:
    largest_element = second_largest_element = SMALLEST_INTEGER
    for i in range(len(arr)):
        if arr[i] > largest_element:
            second_largest_element = largest_element
            largest_element = arr[i]
        elif arr[i] > second_largest_element:
            second_largest_element = arr[i]

    return second_largest_element

print(find_second_largest_element([2,5,1,3,0,-1,-25]))

# Time complexity: O(n)
# Space complexity: O(1)