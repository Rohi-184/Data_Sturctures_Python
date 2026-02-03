class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_front(data)
            return

        new_node = Node(data)
        temp = self.head
        current_index = 0

        while temp is not None and current_index < index - 1:
            temp = temp.next
            current_index += 1

        if temp is None:
            print("Index out of range.")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_front(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        deleted_value = self.head.data
        self.head = self.head.next
        print(f"Node with value {deleted_value} deleted.")

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            print(f"Node with value {deleted_value} deleted.")
            return

        prev = None
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None
        print(f"Node with value {temp.data} deleted.")

    def delete_at_index(self, index):
        if index < 0:
            print("Invalid index.")
            return

        if self.head is None:
            print("Linked list is empty.")
            return

        if index == 0:
            self.delete_front()
            return

        prev = None
        temp = self.head
        current_index = 0

        while temp is not None and current_index < index:
            prev = temp
            temp = temp.next
            current_index += 1

        if temp is None:
            print("Index out of range.")
            return

        prev.next = temp.next
        print(f"Node with value {temp.data} deleted.")

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
    print("\n1. Insert, 2. Delete, 3. Search a node, 4. Display list, 5. Exit ")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("\nInsert Menu: 1. Front, 2. End, 3. Index")
        insert_choice = int(input("Enter insert choice (1-3): "))
        if insert_choice == 1:
            data = int(input("Enter value to insert at front: "))
            llist.insert_front(data)
            print("Node inserted.")
        elif insert_choice == 2:
            data = int(input("Enter value to insert at end: "))
            llist.insert_end(data)
            print("Node inserted.")
        elif insert_choice == 3:
            index = int(input("Enter index (0-based): "))
            data = int(input("Enter value to insert: "))
            llist.insert_at_index(index, data)
        else:
            print("Invalid insert choice! Please enter 1 to 3.")

    elif choice == 2:
        print("\nDelete Menu: 1. Front, 2. End, 3. Index, 4. By value")
        delete_choice = int(input("Enter delete choice (1-4): "))
        if delete_choice == 1:
            llist.delete_front()
        elif delete_choice == 2:
            llist.delete_end()
        elif delete_choice == 3:
            index = int(input("Enter index (0-based): "))
            llist.delete_at_index(index)
        elif delete_choice == 4:
            key = int(input("Enter value to delete: "))
            llist.delete_node(key)
        else:
            print("Invalid delete choice! Please enter 1 to 4.")

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
