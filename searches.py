# binary
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target is not found


## Example Usage:
sorted_list = [1, 2, 4, 6, 7, 9]
target_value = 4
result = binary_search(sorted_list, target_value)
print(f"Binary Search: Target {target_value} found at index: {result}")


# linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if the target is found
    return -1  # Return -1 if the target is not found


## Example Usage:
my_list = [4, 7, 2, 9, 1, 6]
target_value = 9
result = linear_search(my_list, target_value)
print(f"Linear Search: Target {target_value} found at index: {result}")
