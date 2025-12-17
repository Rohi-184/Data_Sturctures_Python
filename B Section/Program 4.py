# Queue Declaration
queue = []
MAX = int(input("Enter queue size: "))

# Check Overflow
def is_overflow():
    return len(queue) >= MAX

# Check Underflow
def is_underflow():
    return len(queue) == 0

# Function to add an element in queue (ENQUEUE)
def add():
    if is_overflow():
        print("Queue Overflow! Cannot insert item.")
    else:
        item = input("Enter your item: ")
        if item in queue:
            print("Duplicate value not allowed!")
        else:
            queue.append(item)
            print("Item inserted:", item)

# Function to remove an element in queue (DEQUEUE)
def remove():
    if is_underflow():
        print("Queue Underflow! Queue is empty.")
    else:
        e = queue.pop(0)
        print("Item removed:", e)

# Function to display queue
def display():
    if is_underflow():
        print("Queue is empty")
    else:
        print("Current Queue:", queue)

# Menu-driven function
def repeat():
    while True:
        user = input(
            "\na - Add element\n"
            "r - Remove element\n"
            "d - Display queue\n"
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
            print("Queue operation stopped")
            break
        else:
            print("INVALID OPTION")

# Main Program
repeat()
f= input("Do you want to continue yes or no : ")
if f=="yes":
    repeat()
elif f=="no":
    print("The queue operation stopped")
else:
    print("Invalid Key")
