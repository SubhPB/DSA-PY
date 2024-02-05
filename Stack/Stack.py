''' -- Byimaan -- '''

class Stack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.topIndex = -1

    def push(self, val): 
        if self.topIndex < self.capacity - 1:
            self.topIndex += 1 
            self.array[self.topIndex] = val
            return val
        else:
            print('Stack overflowed!. ') 

    def pop(self):
        if self.topIndex >= 0:
           val = self.array[self.topIndex]
           self.array[self.topIndex] = None
           self.topIndex -= 1
           return val
           
    def peek(self):
        if self.topIndex >= 0:
            return self.array[self.topIndex]   

    def size(self):
        return self.topIndex + 1; 

    def extend_capacity(self,size=0):
        self.array += [None]*size

    def is_empty(self):
        return self.topIndex == -1
      


if __name__ == '__main__':
    stack = Stack(5)
    stack.push(12)
    for i in range(5):
        stack.push(i + 1)

    for i in range(8):
        stack.pop()

    print(stack.array)    

    