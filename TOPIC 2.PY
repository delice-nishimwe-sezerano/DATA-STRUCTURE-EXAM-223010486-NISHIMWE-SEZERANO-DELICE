# Topic.2:Implement Binary Search Tree (BST) to manage data in the fitness club membership management system.

class Node:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, member_id, name, membership_type):
        new_member = Node(member_id, name, membership_type)
        if self.root is None:
            self.root = new_member
        else:
            self._insert(self.root, new_member)

    def _insert(self, node, new_member):
        if new_member.member_id < node.member_id:
            if node.left is None:
                node.left = new_member
            else:
                self._insert(node.left, new_member)
        else:
            if node.right is None:
                node.right = new_member
            else:
                self._insert(node.right, new_member)

    def search(self, member_id):
        return self._search(self.root, member_id)

    def _search(self, node, member_id):
        if node is None or node.member_id == member_id:
            return node
        if member_id < node.member_id:
            return self._search(node.left, member_id)
        return self._search(node.right, member_id)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"Member ID: {node.member_id}, Name: {node.name}, Membership: {node.membership_type}")
            self.inorder(node.right)

# Example usage
bst = BST()
bst.insert(102, "John Doe", "Premium")
bst.insert(101, "Jane Smith", "Basic")
bst.insert(105, "Alice Brown", "VIP")

print("Inorder traversal (Sorted members by ID):")
bst.inorder(bst.root)
