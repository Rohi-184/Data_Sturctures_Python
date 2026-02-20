import heapq

pq = []   # empty heap (priority queue)

heapq.heappush(pq, (3, "Task C"))
heapq.heappush(pq, (1, "Task A"))
heapq.heappush(pq, (2, "Task B"))
heapq.heappush(pq, (5, "Task D"))
heapq.heappush(pq, (4, "Task E"))
heapq.heappush(pq, (0, "Task X"))



print("Items added to the queue:", pq)

highest_priority_item = heapq.heappop(pq)
print("\nRemoved highest priority item:", highest_priority_item)

print("\nQueue after removal:", pq)

print("\nOutput:")
while pq:
    print(heapq.heappop(pq))
