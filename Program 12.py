import heapq

class PriorityQueue:
    def __init__(self, capacity):
        self.heap = []
        self.count = 0
        self.capacity = capacity

    def insert(self, priority, value):
        if len(self.heap) >= self.capacity:
            print("--- Error: Heap is full! ---")
            return
        heapq.heappush(self.heap, (priority, self.count, value))
        self.count += 1
        print(f"Success: '{value}' added.")

    def delete(self):
        if not self.heap:
            print("--- Error: Heap is empty! ---")
            return None
        item = heapq.heappop(self.heap)
        print(f"Deleted: {item[2]} (Priority: {item[0]})")
        return item[2]

    def display(self):
        if not self.heap:
            print("--- Queue is empty ---")
            return
        print("\n--- Current Priority Queue ---")
        for item in sorted(self.heap):
            print(f"Priority: {item[0]} | Value: {item[2]}")

# User Interaction Setup
limit = int(input("Enter max capacity of the heap: "))
pq = PriorityQueue(limit)

while True:
    print("\n1. Insert  2. Delete  3. Display  4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        try:
            val = input("Enter value: ")
            pri = int(input("Enter priority (lower number = higher priority): "))
            pq.insert(pri, val)
        except ValueError:
            print("Invalid input! Priority must be an integer.")

    elif choice == '2':
        pq.delete()

    elif choice == '3':
        pq.display()

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again.")
