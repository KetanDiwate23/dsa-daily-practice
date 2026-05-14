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

SL = SinglyLinkedlist()
while True:
    print("\n--- STACK MENU ---")
    print("1. insertion at beginning")
    print("2. insertion at end")
    print("3. deletion")
    print("4. display")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        SL.insertion_at_beginning(data=int(input("Enter the data to insert: ")))
    elif choice == 2:
        SL.insertion_at_end(data=int(input("Enter the data to insert: ")))

    elif choice == 3:
        SL.deletion(data=int(input("Enter the data to delete: ")))

    elif choice == 4:
        SL.display()


    else :
        print("Enter a valid choice")