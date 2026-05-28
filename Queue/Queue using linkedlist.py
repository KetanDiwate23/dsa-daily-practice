class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue_using_Linkedlist:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.front is None and self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        else:
            self.rear.next = new_node
            self.rear = new_node

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,end=" -> ")
                temp = temp.next
            print("None")

q=Queue_using_Linkedlist()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
