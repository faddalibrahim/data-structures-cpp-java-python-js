class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.bst_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def insert(self,new_val):
        self.bst_insert(self.root,new_val)

    def bst_search(self, current, find_val):
        if current:
            if current.value == find_val: 
                return True
            elif current.value > find_val:
                return self.bst_search(current.left,find_val)
            elif current.value < find_val:
                return self.bst_search(current.right,find_val)
        return False

    def bst_insert(self,current,new_val):
        if current.value > new_val:
            if current.left:
                self.bst_insert(current.left,new_val)
            else:
                current.left = Node(new_val)
        
        if current.value < new_val:
            if current.right:
                self.bst_insert(current.right,new_val)
            else:
                current.right = Node(new_val)

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal