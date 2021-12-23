class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def __str__(self):
        llist = "[ "

        current = self.head

        while current:
            llist += str(current.value) + " -> "
            current = current.next

        llist += "None ]"

        return llist

    def is_empty(self):
        return self.head == None

    def add_first(self,value):
        new_node = Node(value)

        # list is empty
        if self.is_empty():
            self.head = self.tail = new_node
            self.__size += 1
            return

        # list not empty
        new_node.next = self.head
        self.head = new_node

        self.__size += 1

    def add_last(self,value):
        new_node = Node(value)

        # list is empty
        if self.is_empty():
            self.__size += 1
            self.head = self.tail = new_node
            return

        # list not empty
        self.tail.next = new_node
        self.tail = new_node

        self.__size += 1

    def delete_first(self):
        if self.is_empty():
            raise TypeError("value is None")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        second = self.head.next
        self.head.next = None
        self.head = second

    
    def delete_last(self):
        if self.is_empty():
            raise TypeError("value is None")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        penultimate = self.get_penultimate()
        self.tail = penultimate
        self.tail.next = None

    def get_penultimate(self):
        penultimate = self.head

        while penultimate.next != self.tail:
            penultimate = penultimate.next

        return penultimate

    def index_of(self,value):
        current_node = self.head
        index = 0

        while current_node:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1

        return -1

    def contains(self,value):
        return self.index_of(value) != -1

    def get_size(self):
        return self.__size

    def value_at(self,input_index):
        current_node = self.head

        index = 0
        while current_node:
            if index == input_index:
                return current_node.value

            index += 1
            current_node = current_node.next
        
        raise IndexError("index out of range")

    def reverse(self):
        if self.is_empty():
            return

        previous = self.head
        current = self.head.next

        while current:
            nextt = current.next

            #reverse
            current.next = previous

            #advance pointers
            previous = current
            current = nextt

        #reset head and tail
        self.tail = self.head
        self.tail.next = None
        self.head = previous

        


   

ll = LinkedList()
# print(ll.head.next)
ll.add_last(90)
ll.add_last(67)
ll.add_last(34)
ll.add_last(100)

print(ll)
ll.reverse()
print(ll)
print(ll)

print(ll.tail == ll.head)
# print(ll.head.value)

# print(ll.value_at(0))
# ll.__size = 100
# print(ll.__size)

# ll.add_first(12)
# ll.add_first(90)
# ll.add_first(67)
# ll.add_first(34)

# print(ll)

# print(ll)
# ll.delete_first()
# print(ll)
# ll.delete_first()
# ll.delete_first()
# ll.delete_first()
# ll.delete_last()
# ll.delete_last()
# ll.delete_last()
# ll.delete_last()
# ll.delete_last()
# print(ll)