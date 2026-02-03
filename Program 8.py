class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
        new_node.prev = temp

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
    print("\n1. Insert at end, 2. Delete a node, 3. Search a node, 4. Display list, 5. Exit ")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        data = int(input("\nEnter value to insert: "))
        dll.insert_end(data)
        print("Node inserted.")

    elif choice == 2:
        key = int(input("\nEnter value to delete: "))
        dll.delete_node(key)

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
