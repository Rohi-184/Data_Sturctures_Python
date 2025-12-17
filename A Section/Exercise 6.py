# Stack implementation using list
stack = []

# Taking number of elements from user
n = int (input ("Enter number of elements to push into stack: "))

# Push operation
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    stack.append(element)

print("\nInitial stack")
print(stack)

# Pop operation
print("\nElements popped from stack:")
while stack:
    print(stack.pop())


print("\nStack after elements are popped:")
print(stack)

