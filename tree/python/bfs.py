from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def bfs_iterative(self):
        if not self.root:
            return
        
        q = deque()
        q.append(self.root)

        while len(q):
            current = q.popleft()
            print(current.value)

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    def includes(self,target ):
        q = deque()
        q.append(self.root)
        
        while len(q):
            current = q.popleft()
            
            if current.value == target :
                return True
                
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
                
        return False

    def sum(self):
        q = deque()
        q.append(self.root)
        
        summ = 0
        
        while len(q):
            current = q.popleft()
            
            summ += current.value
                
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
                
        return summ

    def min(self):
        q = deque()
        q.append(self.root)
        
        minn = self.root.value
        
        while len(q):
            current = q.popleft()
            
            if current.value < minn:
                minn = current.value
                
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
                
        return minn

    def max(self):
        q = deque()
        q.append(self.root)
        
        maxx = self.root.value
        
        while len(q):
            current = q.popleft()
            
            if current.value > maxx:
                maxx = current.value
                
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
                
        return maxx


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

# tree.bfs_iterative()
print(tree.max())