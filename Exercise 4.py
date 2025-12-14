# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, search left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else search right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


# Taking sorted array input at runtime
arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))

# Taking element to search
x = int(input("Enter element to search: "))

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print("Element is not present in array")
