#Topic.6:Implement a tree to represent hierarchical data in the fitness club membership management system.

class TreeNode:
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print("  " * level + f"{self.name} ({self.tier})")
        for child in self.children:
            child.display(level + 1)

# Example usage
root = TreeNode("Fitness Club", "Root")
basic_tier = TreeNode("Basic Membership", "Tier 1")
premium_tier = TreeNode("Premium Membership", "Tier 2")

root.add_child(basic_tier)
root.add_child(premium_tier)

premium_tier.add_child(TreeNode("VIP", "Tier 3"))

root.display()
