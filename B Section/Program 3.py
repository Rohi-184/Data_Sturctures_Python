# Stack Declaration
stack = []
MAX = int(input("Enter stack size: "))

# Check Overflow
def is_overflow():
    return len(stack) >= MAX

# Check Underflow
def is_underflow():
    return len(stack) == 0

def add():
    if is_overflow():
        print("Stack Overflow! Cannot insert item.")
    else:
        item = input("Enter your item: ")
        if item in stack:
            print("Duplicate value not allowed!")
        else:
            stack.append(item)
            print("Item inserted:", item)

def remove():
    if is_underflow():
        print("Stack Underflow! Stack is empty.")
    else:
        e = stack.pop()
        print("Item removed:", e)

def display():
    if is_underflow():
        print("Stack is empty")
    else:
        print("Current Stack:", stack)

def repeat():
    while True:
        user = input(
            "\na - Add element\n"
            "r - Remove element\n"
            "d - Display stack\n"
            "e - Exit\n"
            "\nEnter your choice: "
        )

        if user == "a":
            add()
        elif user == "r":
            remove()
        elif user == "d":
            display()
        elif user == "e":
            print("The stack operation is stopped!")
            break
        else:
            print("INVALID OPTION")

# Main Program
repeat()
f= input("Do you want to continue yes or no : ")
if f=="yes":
    repeat()
elif f=="no":
    print("The stack operation stopped")
else:
    print("Invalid Key")
