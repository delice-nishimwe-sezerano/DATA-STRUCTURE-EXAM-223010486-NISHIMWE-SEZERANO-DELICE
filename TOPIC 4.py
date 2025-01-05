#Topic.4:Create Deque to manage a fixed number of orders in the fitness club membership management system.

from collections import deque

class FitnessClubDeque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.deque = deque()

    def add_order(self, order):
        if len(self.deque) >= self.max_size:
            self.deque.popleft()  # Remove oldest order if deque is full
        self.deque.append(order)  # Add new order to the end

    def show_orders(self):
        print("Current Orders:")
        for order in self.deque:
            print(order)

# Example usage
fitness_deque = FitnessClubDeque(3)
fitness_deque.add_order("Yoga - John Doe")
fitness_deque.add_order("Pilates - Jane Smith")
fitness_deque.add_order("Zumba - Alice Brown")
fitness_deque.add_order("Crossfit - Bob Martin")

fitness_deque.show_orders()
