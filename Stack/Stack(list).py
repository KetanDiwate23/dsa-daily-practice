class Stack:
    def __init__(self,size):
        self.top = -1
        self.size = size
        self.stack = []

    def push(self,element):
        if(self.top == self.size-1):
            print("stack is Overflow")
            return
        else:
            self.top += 1
            self.stack.append( element)
            print(element," is pushed to stack at ",self.top," position")

    def pop(self):
        if self.top == -1:
            print("stack is empty")
        else:
            popped = self.stack.pop()
            self.top -= 1
            print(popped,"is popped from stack at")


    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top,-1,-1):
                print(self.stack[i])

size=int(input("enter the size of the stack: "))
s=Stack(size)
while True:

    choice= int(input("enter your choice\n1.Push\n2.Pop\n3.Display\n4.Exit "))
    if choice==1:
        x=int(input("enter the element"))
        s.push(x)
    elif choice==2:
        s.pop()
    elif choice==3:
        s.display()
    elif choice==4:
        break