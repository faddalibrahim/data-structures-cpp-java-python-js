# preorder, inorder, postorder, level order, vertical
# BFS, DFS ( recursive and iterative)
# insertion, deletion, searching


from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value = None):
        if root_value is not None:
            self.root = Node(root_value)
            return
        self.root = root_value

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
            return

        self.level_order_insertion(value,self.root)

    def level_order_insertion(self,value,current):
        q = deque()
        q.append(current) 

        while q:
            curr = q.popleft()

            if not curr.left:
                curr.left = Node(value)
                return
            if not curr.right:
                curr.right = Node(value)
                return

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val: 
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self,start,traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal


# tree = BinaryTree("D")
# tree.insert("B")
# tree.insert("E")
# tree.insert("A")
# tree.insert("C")
# tree.insert("F")

# print(tree.search("A"))
# print(tree.search("B"))
# print(tree.search("C"))
# print(tree.search("D"))
# print(tree.search("E"))
# print(tree.search("F"))
# print(tree.search("G"))
# tree.insert(12)
# print(tree.preorder_print(tree.root,""))
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
#   4  5

# Test search
# Should be True
# print(tree.search(4))
# Should be False
# print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
# print(tree.print_tree())

print(tree.preorder_print(tree.root,"")[:-1])
# print(tree.inorder_print(tree.root,"")[:-1])
# print(tree.postorder_print(tree.root,"")[:-1])







