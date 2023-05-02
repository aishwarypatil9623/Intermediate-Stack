class Stack:
    def __init__(self, capacity):
        self.capacity = capacity                                                 # set the maximum size of the stack
        self.stack = []                                                          # initialize an empty list as the stack

    def push(self, element):
        if self.isFull():                                                        # check if the stack is full
            print("Stack Overflow")
        else:
            self.stack.append(element)                                           # add the element to the top of the stack

    def pop(self):
        if self.isEmpty():                                                       # check if the stack is empty
            print("Stack Underflow")
        else:
            return self.stack.pop()                                              # remove and return the top element from the stack

    def peek(self):
        if self.isEmpty():                                                       # check if the stack is empty
            print("Stack Underflow")
        else:
            return self.stack[-1]                                                # return the top element of the stack without removing it

    def size(self):
        return len(self.stack)                                                   # return the number of elements in the stack

    def isEmpty(self):
        return len(self.stack) == 0                                              # check if the stack is empty and return a boolean value

    def isFull(self):
        return len(self.stack) == self.capacity                                  # check if the stack is full and return a boolean value

# usage example
if __name__ == '__main__':
    myStack = Stack(5)                                                           # create a stack with a maximum capacity of 5

    myStack.push(10)                                                             # push elements onto the stack
    myStack.push(20)
    myStack.push(30)

    print(myStack.pop())                                                        # pop an element from the stack

    print(myStack.peek())                                                       # peek at the top element of the stack

    print(myStack.size())                                                       # get the current size of the stack

    print(myStack.isEmpty())                                                    # check if the stack is empty

    print(myStack.isFull())                                                     # check if the stack is full
