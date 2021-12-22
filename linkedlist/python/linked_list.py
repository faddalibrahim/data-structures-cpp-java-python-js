class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def add_first(self,value):
        new_node = Node(value)

        # list is empty
        if not self.head:
            self.head = self.tail = new_node
            return

        # list not empty
        new_node.next = self.head
        self.head = new_node

    def add_last(self,value):
        new_node = Node(value)

        # list is empty
        if not self.head:
            self.head = self.tail = new_node
            return

        # list not empty
        self.tail.next = new_node
        self.tail = new_node

    def delete_first(self):
        if not self.head:
            raise TypeError("value is None")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        second = self.head.next
        self.head.next = None
        self.head = second

    
    def delete_last(self):
        if not self.tail:
            raise TypeError("value is None")

        if self.head == self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next

        self.tail = current
        current.next = None


   

ll = LinkedList()
# print(ll.head.next)
# ll.add_last(90)
# ll.add_last(67)
# ll.add_last(34)

ll.add_first(12)
# ll.add_first(90)
# ll.add_first(67)
# ll.add_first(34)

# print(ll)

# print(ll)
# ll.delete_first()
print(ll)
ll.delete_last()
print(ll)