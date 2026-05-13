class Queue:
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.queue = []

    def enqueue(self, element):
        if self.rear == self.size - 1:
            print("Queue is overflow")
            return
        else:
            if self.front == -1:
                self.front = 0

            self.queue.append(element)
            self.rear += 1
            print(self.queue, self.rear, "is added to queue at", self.rear, "position")

    def dequeue(self):
        if self.front == -1 :
            print("Queue is empty")
            return
        else:
            deleted = self.queue[self.front]
            print(deleted,"is deleted from queue at ",self.front," position")
            self.front=self.front+1

    def display(self):
        if self.front == -1 :
            print("Queue is empty")
            return
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])

size = int(input("enter the size of the queue: "))
s = Queue(size)
while True:
        choice = int(input("enter your choice\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit "))
        if choice == 1:
            x = int(input("enter the element"))
            s.enqueue(x)
        elif choice == 2:
            s.dequeue()
        elif choice == 3:
            s.display()
        elif choice == 4:
            break