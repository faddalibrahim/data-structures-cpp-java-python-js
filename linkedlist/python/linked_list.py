class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        # self.prev = None

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

        deleted_value = self.tail.value
        
        #reset tail
        penultimate = self.get_penultimate()
        self.tail = penultimate
        self.tail.next = None

        return deleted_value

    # def delete_node_at(self,position):
    #     if is_empty():
    #         raise IndexError

    #     index = 0
    #     current = self.head


        

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

    def recursive_reverse(self,head,prev):
        if not head:
            return

        self.recursive_reverse(head.next,head)
        head.next = prev

        if head == self.tail:
            self.head = head
        
        if head.next == None:
            self.tail = head

    def kth_node(self,k):
        pointer_1 = self.head
        pointer_2 = self.head

        index = 0

        #setting the second pointer
        while index < k:
            pointer_2 = pointer_2.next
            index += 1

        #finding kth node
        while pointer_2:
            pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next

        return pointer_1.value

    def print_reverse(self,head):
        if not head:
            return

        self.print_reverse(head.next)
        print(head.value)

    def make_doubly_linked(self,head,prev):
        if not head:
            return

        self.make_doubly_linked(head.next,head)
        head.prev = prev

    # def clone()
    # def detect_cycle()
    # def to_array()

ll = LinkedList()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)

print(ll)

ll.recursive_reverse(ll.head,None)

print(ll)

ll.reverse()

print(ll)