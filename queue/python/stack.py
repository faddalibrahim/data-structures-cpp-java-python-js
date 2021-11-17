stack1 = []
stack2 = []

class Queue:
    stack1 = []
    stack2 = []
    
    def enqueue(self, value):
        if len(self.stack2) != 0:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
            self.stack1.append(value)
        else:
            self.stack1.append(value)
        
    def dequeue(self):
        if len(self.stack2) != 0 and len(self.stack1) == 0:
            return self.stack2.pop()
        elif len(self.stack1) != 0:
            while(len(self.stack1) != 0):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
            
    def __str__(self):
        string = ""
        if len(self.stack1) != 0:
            for item in self.stack1:
                string += str(item) + ", "
            return "[ " + string + "]"
        return string
        
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
# print(q)