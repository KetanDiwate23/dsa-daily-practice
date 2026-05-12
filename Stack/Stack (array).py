class Stack:
    def __init__(self, size):
        self.stack = [0] * size   # user-defined storage
        self.top = -1
        self.size = size

    def push(self, value):
        if self.top == self.size - 1:
            print(" Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f" {value} pushed into stack")

    def pop(self):
        if self.top == -1:
            print(" Stack Underflow")
        else:
            popped = self.stack[self.top]
            self.top -= 1
            print(f" {popped} popped from stack")

    def peek(self):
        if self.top == -1:
            print(" Stack is empty")
        else:
            print(" Top element:", self.stack[self.top])

    def display(self):
        if self.top == -1:
            print(" Stack is empty")
        else:
            print(" Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
size = int(input("Enter stack size: "))
s = Stack(size)

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: \n"))

    if choice == 1:
        val = int(input("Enter value to push: "))
        s.push(val)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print(" Exiting program")
        break

    else:
        print(" Invalid choice")
