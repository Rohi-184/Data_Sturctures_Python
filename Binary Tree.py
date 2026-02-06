import tkinter as tk

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)


# -------- DRAW TREE USING TKINTER --------
class TreeVisualizer:
    def __init__(self, bst):
        self.window = tk.Tk()
        self.window.title("Binary Tree Visualization")
        self.canvas = tk.Canvas(self.window, width=900, height=600, bg="white")
        self.canvas.pack()
        self.radius = 20
        self.draw_tree(bst.root, 450, 50, 200)
        self.window.mainloop()

    def draw_tree(self, node, x, y, gap):
        if node:
            if node.left:
                self.canvas.create_line(x, y, x - gap, y + 150)
                self.draw_tree(node.left, x - gap, y + 150, gap // 2)

            if node.right:
                self.canvas.create_line(x, y, x + gap, y + 150)
                self.draw_tree(node.right, x + gap, y + 150, gap // 2)

            self.canvas.create_oval(
                x - self.radius, y - self.radius,
                x + self.radius, y + self.radius,
                fill="lightgreen"
            )
            self.canvas.create_text(x, y, text=str(node.data), font=("Arial", 12, "bold"), fill="black")


# -------- MAIN --------
bst = BST()

n = int(input("Enter number of nodes: "))
for i in range(n):
    bst.insert(int(input(f"Enter value {i+1}: ")))

TreeVisualizer(bst)
