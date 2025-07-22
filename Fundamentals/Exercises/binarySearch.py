# Sorted list and target
numbers = [1, 3, 5, 6, 7, 8, 11, 15, 20, 21]
target = 15
# Binary search function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1  # Define search bounds
    while low <= high:
        mid = (low + high) // 2  # Find the middle
        if arr[mid] == target:
            return mid  # Return index if found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
    return -1  # Return -1 if not found
# Run binary search and print result
index = binary_search(numbers, target)
if index != -1:
    print("The number {target} is at index ", index,".")
else:
    print("The number {target} was not found.")