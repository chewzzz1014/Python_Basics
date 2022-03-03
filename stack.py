# demonstrate stack using python list and wrapper class
# push, pop, peek, clear

class Stack():

    def __init__(self):
        self.stack = list()

    def push(self, *item):
        if len(item)==1:
            self.stack.append(item)
        else:
            self.stack.extend(item)

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

    def clear(self):
        del(self.stack)


myStack = Stack()
myStack.pop()
myStack.push(2,3,4)
print(myStack.__str__())




