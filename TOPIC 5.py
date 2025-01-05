#Topic.5:Use Heap to track data dynamically in fitness club membership management system.

import heapq

class FitnessClubHeap:
    def __init__(self):
        self.heap = []

    def add_member(self, priority, name):
        heapq.heappush(self.heap, (priority, name))

    def process_member(self):
        return heapq.heappop(self.heap) if self.heap else None

    def show_members(self):
        for priority, name in self.heap:
            print(f"Priority: {priority}, Name: {name}")

# Example usage
fitness_heap = FitnessClubHeap()
fitness_heap.add_member(1, "John Doe")
fitness_heap.add_member(3, "Jane Smith")
fitness_heap.add_member(2, "Alice Brown")

fitness_heap.show_members()
print("Processing the highest priority member:", fitness_heap.process_member())
