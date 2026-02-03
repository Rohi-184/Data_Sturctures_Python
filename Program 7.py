class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            print(f"Node with value {key} deleted.")
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found in the list.")
            return

        prev.next = temp.next
        print(f"Node with value {key} deleted.")

    def search(self, key):
        """Search for a value in the linked list."""
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print(f"Value {key} found at position {position}.")
                return
            temp = temp.next
            position += 1

        print(f"Value {key} not found in the list.")

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")



llist = LinkedList()

while True:
    print("\n1. Insert at end, 2. Delete a node, 3. Search a node, 4. Display list, 5. Exit ")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        data = int(input("Enter value to insert: "))
        llist.insert_end(data)
        print("Node inserted.")

    elif choice == 2:
        key = int(input("Enter value to delete: "))
        llist.delete_node(key)

    elif choice == 3:
        key = int(input("Enter value to search: "))
        llist.search(key)

    elif choice == 4:
        print("Linked List:")
        llist.display()

    elif choice == 5:
        print("Exiting program....")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
