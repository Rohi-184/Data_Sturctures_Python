class MergeSort_ADT:
    def __init__(self):
        self.arr = []

    def get_input(self):
        self.arr = []
        n = int(input("Enter the number of elements: "))
        for i in range(n):
            item = int(input(f"Enter element {i+1}: "))
            self.arr.append(item)
        print("Elements inserted successfully")

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_display(self):
        if not self.arr:
            print("Array is Empty")
        else:
            print("Before Sorting:", self.arr)
            sorted_arr = self.merge_sort(self.arr)
            print("After Sorting :", sorted_arr)


s = MergeSort_ADT()

def rep():
    while True:
        print("\nGiven Choices are available")
        print("1 is Enter Elements")
        print("2 is Sort using Merge Sort")
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
        print("The Merge Sort Process was Stopped!")
        break
    else:
        print("Invalid Typing")
