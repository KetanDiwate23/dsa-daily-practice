class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def display(self):
        temp = self.root
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    def sort(self):
            temp = self.root
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
        temp = self.root                         # traversing
        p = 0                      # for counting
        while temp is not None:             # loop starts
            if temp.data == data:    # if search data matches with the lement in linkedlist
                print(data," found at position ",p)
                return
            temp= temp.next
            p+=1
        print(data," not found ")

    def insert_on_front(self,data):
        new_node = Node(data)

        if self.root is None:
           self.root = new_node

        else:
            new_node.next = self.root
            self.root = new_node

        print(data," added at begining of Linked List")

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

        print(data," added to the end of Linked List")

    def count(self):
        if self.root is None:
            print("Linked List is empty")
            return
        temp = self.root
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_at_position(self,data):
        new_node = Node(data)
        p = int(input("Enter the position: "))
        if p < 0 or p > self.count():
            print("Invalid Position")
            return
        elif p == 0:
            new_node.next = self.root
            self.root = new_node
            return
        else:
            temp = self.root
            for i in range(p-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            print(data," added at",p,"position of Linked List")


    def delete_element(self,data):
        temp = self.root
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Element Not Found")
            return

        if prev is None:
            self.root = temp.next
        else:
            prev.next = temp.next
        del temp
        print(data," deleted from Linked List")

sll = LinkedList()
while True:
    print("--MENU--\n1.Add node at front\n2.Add at end\n3.Delete Element\n4.Insert in Between\n5.Display Linked List\n6.Sort Linklist\n7.Exit\n8.search node")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        element = int(input("Enter the element:"))
        sll.insert_on_front(element)

    elif choice == 2:
        element = int(input("Enter the element:"))
        sll.insert_at_end(element)

    elif choice == 3:
        element = int(input("Enter the element:"))
        sll.delete_element(element)

    elif choice == 4:
        element = int(input("Enter the element:"))
        sll.insert_at_position(element)

    elif choice == 5:
        sll.display()

    elif choice == 6:
        sll.sort()

    elif choice == 7:
        print("Thank you for using this program")
        break

    elif choice == 8:
        sll.search_node(data=int(input("Enter the element:")))

    else:
        print("Invalid Choice")