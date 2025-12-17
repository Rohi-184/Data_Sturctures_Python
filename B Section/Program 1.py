# Taking list input from user
L1 = []

n = int(input("Enter Number of elements you want to add : "))
for z in range(0,n):
    a = int(input(f"Enter the element {z} : "))
    L1.append(a)

# Taking element to search
x = int(input("\nEnter element to search: "))

i = 0  # pointer

while (i < len(L1)):
    if L1[i]==x:
        print(f'Element {x} present at {i}th position')
        break
    i += 1

if i >= len(L1):
    print('Element is not present')
