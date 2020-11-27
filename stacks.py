# Stacks Demo

class Stack():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.contents = [ None for i in range(maxsize)]
        self.top = -1
    
    def push(self, newItem):
        if self.top == self.maxsize-1:
            print("The Stack is full")
        else:
            self.top += 1
            self.contents[self.top] = newItem
            
    def printAll(self):
        for item in self.contents:
            print(item)
        
    def pop(self):
        if self.top == -1:
            print("The Stack is Empty")
        else:
            itemtoreturn = self.contents[self.top]
            self.top -= 1
            return itemtoreturn
    
    
        

myStack = Stack(5)
# myStack.push("Harry")
# myStack.push("Maggy")
# myStack.push("Lenny")
# myStack.push("Wendy")
# myStack.push("Bobby")
print(  myStack.pop()  )




