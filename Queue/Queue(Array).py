class Queue:
    def __init__(self,size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [0] * size

    def enqueue(self,element):
        if self.rear == self.size - 1:
            print(" Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue[self.rear] = element
            print(element," is added to queue at ",self.rear)

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print(" Queue is Empty")
        else:
            deleted = self.queue[self.front]
            print(deleted," is deleted ")
            i=0
            while i<self.rear:
                self.queue[i] = self.queue[i+1]
                i += 1
        self.rear -= 1


    def display(self):
        if self.front == -1 or self.front > self.rear:
            print(" Queue is Empty")
        else:
            for i in range(self.front,self.rear + 1):
                print(self.queue[i])

size = int(input("Enter queue size: "))
q = Queue(size)

while True:
    print("\n--- Queue Menu ---\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter v1alue to enqueue: "))
        q.enqueue(val)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")