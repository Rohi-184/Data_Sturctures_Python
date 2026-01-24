class QuickSort_ADT:
    def __init__(self):
        self.arr = []

    def get_input(self):
        self.arr = []
        n = int(input("Enter the number of elements: "))
        for i in range(n):
            item = int(input(f"Enter element {i+1}: "))
            self.arr.append(item)
        print("Elements inserted successfully")

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)

    def sort_display(self):
        if not self.arr:
            print("Array is Empty")
        else:
            print("Before Sorting:", self.arr)
            self.quick_sort(self.arr, 0, len(self.arr) - 1)
            print("After Sorting :", self.arr)


s = QuickSort_ADT()

def rep():
    while True:
        print("\nGiven Choices are available")
        print("1 is Enter Elements")
        print("2 is Sort using Quick Sort")
        print("3 is Exit the process")

        ch = int(input("Enter the Choice: "))

        if ch == 1:
            s.get_input()
        elif ch == 2:
            s.sort_display()
        elif ch == 3:
            print("Exit the Process")
            break
        else:
            print("Invalid Choice")


rep()

while True:
    d = input("\nDo you want to continue? (yes/no): ").lower()
    if d == "yes":
        rep()
    elif d == "no":
        print("The Quick Sort Process was Stopped!")
        break
    else:
        print("Invalid Typing")
