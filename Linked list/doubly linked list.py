class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def insertion_at_front(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(data," added to the beginning of the list")

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(data," added to the end of the list")

    def count(self):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_at_any_position(self,data):
        new_node = Node(data)
        pos =int(input("Enter position to insert: "))
        if p > 0 or pos < self.count():
            print('Invalid Position')
            return



    def display(self):
        temp = self.head

        while temp:
            print(temp.data, ' <-> ', end=' ')
            temp = temp.next
        print('None')

DL = DoublyLinkedlist()
while True:
    print("\n--- STACK MENU ---")
    print("1. insertion at beginning")
    print("2. Append")
    print('3.Count')
    print('4.insert at any position')
    print('5.Delete element')
    print('6.display')
    print('7.Sort')
    print('8.Search node')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        DL.insertion_at_front(data=int(input("Enter element to insert: ")))

    elif choice == 2:
        DL.append(data=int(input("Enter element to insert: ")))

    elif choice == 3:
        print('total number of elements: ', DL.count())

    elif choice == 6:
        DL.display()
