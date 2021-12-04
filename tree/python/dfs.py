from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def dfs_preorder_iterative(self):
        if not self.root:
            return
        stack = [self.root]; 
        while len(stack) > 0:
            current = stack.pop()
            print(current.value, end = " ")

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def dfs_preorder_recursive(self,start,values):
        if start:
            values += [start.value]
            left_values = values + self.dfs_preorder_recursive(start.left,values)
            right_values = values + self.dfs_preorder_recursive(start.right,values)

        return values

    def includes(self, start, target):
        if start:
            if start.value == target: 
                return True
            else:
                return self.includes(start.left, target) or self.includes(start.right, target)
        return False

    def sum(self,start):
        if not start:
            return 0
        return start.value + self.sum(start.left) + self.sum(start.right)

    def min_recursive(self,start):
        if not start:
            return float('inf')

        leftMin = self.min_recursive(start.left)
        rightMin = self.min_recursive(start.right)

        return min(start.value,leftMin, rightMin)

    def max_recursive(self,start):
        if not start:
            return -float('inf')

        leftMin = self.max_recursive(start.left)
        rightMin = self.max_recursive(start.right)

        return max(start.value,leftMin, rightMin)




# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3) 
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

#       1
#      / \
#     2   3
#    / \
#    4  5

# Test search
# Should be True
# print(tree.search(4))
# Should be False
# print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
# print(tree.print_tree())

# tree.depth_first_values()
# print(tree.dfs_preorder_recursive(tree.root,[]))

# print(tree.min_recursive(tree.root))
print(tree.max_recursive(tree.root))