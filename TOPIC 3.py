# Topic.3:Implement Binary Search Tree (BST) to manage data in the fitness club membership management system.

class TreeNode:
    def __init__(self, member_id, name, membership_type):
        self.member_id = member_id
        self.name = name
        self.membership_type = membership_type
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, member_id, name, membership_type):
        new_member = TreeNode(member_id, name, membership_type)
        if self.root is None:
            self.root = new_member
        else:
            self._insert(self.root, new_member)

    def _insert(self, node, new_member):
        if node.left is None:
            node.left = new_member
        elif node.right is None:
            node.right = new_member
        else:
            self._insert(node.left, new_member)  # For simplicity, always trying to insert to the left first

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"Member ID: {node.member_id}, Name: {node.name}, Membership: {node.membership_type}")
            self.inorder(node.right)

# Example usage
bt = BinaryTree()
bt.insert(101, "John Doe", "Basic")
bt.insert(102, "Jane Smith", "Premium")
bt.insert(103, "Alice Brown", "VIP")

print("Inorder traversal:")
bt.inorder(bt.root)
