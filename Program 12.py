import heapq

def main():
    pq = []
    while True:
        print("\n--- Heap Menu ---")
        print("1. Insert Value (Int or Char)")
        print("2. Delete (Min or Max)")
        print("3. Display (Min and Max)")
        print("4. Display All (Sorted)")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            val = input("Enter value to insert: ")
            if val.isdigit():
                val = int(val)
            heapq.heappush(pq, val)
            print(f"Inserted Value: {val}")

        elif choice == '2':
            if not pq:
                print("Queue is empty!")
                continue

            print("  a. Delete Highest Priority (Min)")
            print("  b. Delete Lowest Priority (Max)")
            print("  c. Delete Particular Value")
            sub_choice = input("  Select (a/b/c): ").lower()

            if sub_choice == 'a':
                removed = heapq.heappop(pq)
                print(f"Removed Minimum: {removed}")

            elif sub_choice == 'b':
                maximum = max(pq)
                pq.remove(maximum)
                heapq.heapify(pq)
                print(f"Removed Maximum: {maximum}")

            elif sub_choice == 'c':
                key = input("Enter Value to delete: ")
                if key.isdigit():
                    key = int(key)
                if key in pq:
                    pq.remove(key)
                    heapq.heapify(pq)
                    print(f"Removed {key}")
                else:
                    print(f"Value {key} is not present in the queue.")

            else:
                print("Invalid selection.")

        elif choice == '3':
            if pq:
                print(f"Highest Priority (Smallest): {pq[0]}")
                print(f"Lowest Priority (Largest): {max(pq)}")
            else:
                print("Queue is empty.")

        elif choice == '4':
            if pq:
                print("All elements in priority order:", sorted(pq))
            else:
                print("Queue is empty.")

        elif choice == '5':
            print("Exiting......")
            break

        else:
            print("Invalid choice. Try again.")

main()