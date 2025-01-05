#Topic.7:Implement a tree to represent hierarchical data in the fitness club membership management system.

def insertion_sort(members):
    for i in range(1, len(members)):
        key = members[i]
        j = i - 1
        while j >= 0 and key[0] < members[j][0]:
            members[j + 1] = members[j]
            j -= 1
        members[j + 1] = key

# Example usage
members = [(3, "John Doe"), (1, "Jane Smith"), (2, "Alice Brown")]
insertion_sort(members)

for priority, name in members:
    print(f"Priority: {priority}, Name: {name}")
