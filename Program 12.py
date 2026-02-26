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

        choice = input("\nSelect an option: ")

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
            sub_choice = input("  Select (a/b): ").lower()

            if sub_choice == 'a':
                removed = heapq.heappop(pq)
                print(f"Removed Minimum: {removed}")
            elif sub_choice == 'b':
                # Find the max value
                maximum = max(pq)
                # Find its index and remove it
                pq.remove(maximum)
                # Re-establish the heap property
                heapq.heapify(pq)
                print(f"Removed Maximum: {maximum}")
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


if __name__ == "__main__":
    main()