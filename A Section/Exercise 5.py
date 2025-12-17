def binary_search(L, key, low, high):
    if high >= low:
        mid = (low + high) // 2
        if key == L[mid]:
            return mid
        elif key > L[mid]:
            return binary_search(L, key, mid + 1, high)
        else:
            return binary_search(L, key, low, mid - 1)
    else:
        return -1


# Taking sorted list input at runtime
L = list(map(int, input("Enter sorted list elements separated by space: ").split()))

# Taking key input
key = int(input("Enter element to search: "))

# Function call
idx = binary_search(L, key, 0, len(L) - 1)

if idx != -1:
    print(f'In list {L}, the key {key} lies at index : {idx}')
else:
    print('The element is not present in array')
