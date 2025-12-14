# Taking list input from user
L1 = list(map(int, input("Enter list elements separated by space: ").split()))

# Taking element to search
x = int(input("Enter element to search: "))

i = 0  # pointer

while i < len(L1):
    if L1[i] == x:
        print(f'Element {x} present at {i}th position')
        break
    i += 1

if i >= len(L1):
    print('Element is not present')
