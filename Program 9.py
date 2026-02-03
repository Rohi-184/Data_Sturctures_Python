class Node:
    """Node in the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with level-based search and all traversals."""
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    # Search with level
    def search(self, key):
        level = self._search_level(self.root, key, 1)
        if level != -1:
            print(f"Value {key} found at level {level}.")
        else:
            print(f"Value {key} not found in the BST.")

    def _search_level(self, root, key, level):
        if root is None:
            return -1
        if root.data == key:
            return level
        elif key < root.data:
            return self._search_level(root.left, key, level + 1)
        else:
            return self._search_level(root.right, key, level + 1)

    # Delete
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            print(f"Value {key} not found in the BST.")
            return root
        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                print(f"Node with value {key} deleted.")
                return root.right
            elif root.right is None:
                print(f"Node with value {key} deleted.")
                return root.left
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Inorder Traversal
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)

    # Preorder Traversal
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root:
            print(root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    # Postorder Traversal
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data, end=" ")


# -------- Menu-Driven Program --------

bst = BinarySearchTree()

while True:
    print("\n1. Insert  2. Delete  3. Search  4. Inorder  5. Preorder  6. Postorder  7. Exit")
    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        bst.insert(value)
        print("Node inserted.")

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        bst.delete(value)

    elif choice == 3:
        value = int(input("Enter value to search: "))
        bst.search(value)

    elif choice == 4:
        print("Inorder Traversal:", end=" ")
        bst.inorder()

    elif choice == 5:
        print("Preorder Traversal:", end=" ")
        bst.preorder()

    elif choice == 6:
        print("Postorder Traversal:", end=" ")
        bst.postorder()

    elif choice == 7:
        print("Program ended")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")
