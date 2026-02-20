class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
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
        new_node.prev = temp

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_front(data)
            return

        temp = self.head
        current_index = 0

        while temp is not None and current_index < index:
            temp = temp.next
            current_index += 1

        if temp is None and current_index == index:
            self.insert_end(data)
            return

        if temp is None:
            print("Index out of range.")
            return

        new_node = Node(data)
        prev_node = temp.prev
        new_node.next = temp
        new_node.prev = prev_node
        if prev_node is not None:
            prev_node.next = new_node
        temp.prev = new_node

    def delete_node(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                print(f"Node with value {key} deleted.")
                return

            temp = temp.next

        print("Value not found in the list.")

    def delete_front(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        deleted_value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
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

        temp = self.head
        while temp.next:
            temp = temp.next

        deleted_value = temp.data
        temp.prev.next = None
        print(f"Node with value {deleted_value} deleted.")

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

        temp = self.head
        current_index = 0

        while temp is not None and current_index < index:
            temp = temp.next
            current_index += 1

        if temp is None:
            print("Index out of range.")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next

        print(f"Node with value {temp.data} deleted.")

    def search(self, key):
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

        # Forward traversal
        print("\nForward traversal:")
        temp = self.head
        last = None
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

        # Backward traversal
        print("\nBackward traversal:")
        while last:
            print(last.data, end=" <-> ")
            last = last.prev
        print("None")



dll = DoublyLinkedList()

while True:
    print("\n1. Insert, 2. Delete, 3. Search a node, 4. Display list, 5. Exit ")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("\nInsert Menu: 1. Front, 2. End, 3. Index")
        insert_choice = int(input("Enter insert choice (1-3): "))
        if insert_choice == 1:
            data = int(input("Enter value to insert at front: "))
            dll.insert_front(data)
            print("Node inserted.")
        elif insert_choice == 2:
            data = int(input("Enter value to insert at end: "))
            dll.insert_end(data)
            print("Node inserted.")
        elif insert_choice == 3:
            index = int(input("Enter index (0-based): "))
            data = int(input("Enter value to insert: "))
            dll.insert_at_index(index, data)
        else:
            print("Invalid insert choice! Please enter 1 to 3.")

    elif choice == 2:
        print("\nDelete Menu: 1. Front, 2. End, 3. Index, 4. By value")
        delete_choice = int(input("Enter delete choice (1-4): "))
        if delete_choice == 1:
            dll.delete_front()
        elif delete_choice == 2:
            dll.delete_end()
        elif delete_choice == 3:
            index = int(input("Enter index (0-based): "))
            dll.delete_at_index(index)
        elif delete_choice == 4:
            key = int(input("Enter value to delete: "))
            dll.delete_node(key)
        else:
            print("Invalid delete choice! Please enter 1 to 4.")

    elif choice == 3:
        key = int(input("\nEnter value to search: "))
        dll.search(key)

    elif choice == 4:
        print("\nLinked List:")
        dll.display()

    elif choice == 5:
        print("\nExiting...")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 5.")
