class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            print(data,"added to stack")
        else:
            new_node.next = self.top
            self.top = new_node
            print(data,"added to stack")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        else:
            tmp = self.top.data
            self.top = self.top.next
            print(tmp,"removed from stack")
            del tmp

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return
        else:
            print('top element of stack is',self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        else:
            print('Stack is')
            temp = self.top
            while temp is not None:
                print(temp.data)
                temp = temp.next


SLL = Stack()
while True:
    print('Stack using linkedlist')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        SLL.push(data=int(input('enter element')))

    elif choice == 2:
        SLL.pop()

    elif choice == 3:
        SLL.peek()

    elif choice == 4:
        SLL.display()
