def linear_search (L, key, i):
    if i >= len(L):
        return -1
    if L[i] == key:
        return i
    return linear_search(L, key, i + 1)

# Taking list input at runtime
L = list(map(int, input("Enter list elements separated by space: ").split()))

# Taking key input
key = int(input("Enter element to search: "))

x = linear_search(L, key, 0)

if x != -1:
    print('List :', L)
    print(f'Element {key} is available at index : {x}')
else:
    print('The element is not present')
