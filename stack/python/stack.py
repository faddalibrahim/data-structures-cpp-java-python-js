import sys
sys.path.insert(0,"c:\\users\\fadda\Desktop\\fav_repos\\data-structures-cpp-java-python-js\\linkedlist\\python")


from linked_list import LinkedList

class Stack(LinkedList):
    def push(self,value):
        self.add_last(value)

    def pop(self):
        return self.delete_last()

    def peek(self):
        return self.tail.value

    def size(self):
        return self.get_size()

st = Stack()
print(st)
st.push(100)
st.push(34)
print(st)
print(st.pop())

