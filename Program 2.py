def binary_search_recursive(arr, low, high, target):
    # Base case: Search space is exhausted
    if low > high:
        return -1

    # Find the middle index
    mid = (low + high) // 2

    # Case 1: Target found at mid
    if arr[mid] == target:
        return mid
    
    # Case 2: Target is smaller than mid, search the left half
    elif target < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, target)
    
    # Case 3: Target is larger than mid, search the right half
    else:
        return binary_search_recursive(arr, mid + 1, high, target)

# Example Usage:
my_list = [10, 22, 35, 47, 50, 63, 75, 88, 99]
target_val = 75

result = binary_search_recursive(my_list, 0, len(my_list) - 1, target_val)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not present in array")