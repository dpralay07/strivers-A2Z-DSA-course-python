# Remove duplicates from sorted array - IN PLACE

def remove_duplicates(arr: list) -> list:
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    
    return arr[:i+1]

print(remove_duplicates([1,1,2,2,2,3,3]))

# Time complexity: O(n)
# Space complexity: O(1)