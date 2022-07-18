class minHeap:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.heap = [] * self.capacity

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def get_left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def get_right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def get_parent(self, index):
        return self.heap[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        self.heap[index_one], self.heap[index_two] = self.heap[index_two], self.heap[index_one]

    def ensure_extra_capacity(self):
        if self.size == self.capacity:
            self.heap = [item for item in self.heap] + ([0]*(self.capacity*2))
            self.capacity *= 2

    def peek(self):
        if self.size == 0:
            raise Exception("heap is empty")

        return self.heap[0]

    def pop(self):
        if self.size == 0:
            raise Exception("heap is empty")

        item = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.size -= 1
        self.heapifyDown()

        return item

    def add(self, item):
        self.ensure_extra_capacity()

        self.heaps[self.size] = item
        self.size += 1

        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1

        while self.has_parent(index) and self.get_parent(index) > self.heaps[index]:
            self.swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)

    def heapifyDown(self):
        index = 0

        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.heaps[index] < self.heaps[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index
