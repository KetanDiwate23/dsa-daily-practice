class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedlist:
    def __init__(self):
        self.head = None

    def insertion_at_beginning(self,data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node

    def insertion_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

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
        p = int(input("Enter the position: "))
        if p < 0 or p > self.count():
            print("Invalid Position")
            return
        elif p == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            temp = self.head
            for i in range(p-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            print(data," added at",p,"position of Linked List")

    def deletion(self, data):
        temp = self.head
        prev = None

        # Search for node
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        # If element not found
        if temp is None:
            print("Element not found")
            return

        # If deleting head node
        if prev is None:
            self.head = temp.next

        else:
            prev.next = temp.next

        del temp
        print('element deleted')


    def display(self):

        temp = self.head


        while temp is not None:
            print(temp.data,'->',end=' ')
            temp = temp.next
        print('None')

    def sort(self):
            temp = self.head
            while temp is not None:
                temp1= temp.next
                while temp1 is not None:
                    if temp.data > temp1.data:
                        k = temp.data
                        temp.data = temp1.data
                        temp1.data = k
                    temp1= temp1.next
                temp = temp.next
            self.display()

    def search_node(self,data):
        temp = self.head                         # traversing
        p = 0                      # for counting
        while temp is not None:             # loop starts
            if temp.data == data:    # if search data matches with the lement in linkedlist
                print(data," found at position ",p)
                return
            temp= temp.next
            p+=1
        print(data," not found ")

SL = SinglyLinkedlist()
while True:
    print("\n--- STACK MENU ---")
    print("1. insertion at beginning")
    print("2. insertion at end or append")
    print('3.Count')
    print('4.insert at any position')
    print('5.Delete element')
    print('6.display')
    print('7.Sort')
    print('8.Search node')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        SL.insertion_at_beginning(data=int(input("Enter the data to insert: ")))
    elif choice == 2:
        SL.insertion_at_end(data=int(input("Enter the data to insert: ")))

    elif choice == 3:
        print("Total Number of nodes",SL.count())

    elif choice == 4:
        SL.insert_at_any_position(data=int(input("Enter the data to insert: ")))

    elif choice == 5:
        SL.deletion(data=int(input("Enter the data to delete: ")))

    elif choice == 6:
        SL.display()

    elif choice == 7:
        SL.sort()

    elif choice == 8:
        SL.search_node(data=int(input("Enter the data to search: ")))

    else :
        print("Enter a valid choice")