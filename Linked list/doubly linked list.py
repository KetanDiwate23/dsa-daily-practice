class Node:

    # EK NODE BAN RAHA HAI
    # Har node ke paas:
    # 1. data
    # 2. next node ka address
    # 3. previous node ka address

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedlist:

    def __init__(self):  # Linked List ka starting point
        self.head = None

    def insertion_at_front(self, data):

        new_node = Node(data) # Naya node create

        if self.head is None: # Agar list empty hai

            self.head = new_node  # Head ko new node bana do

        else:
            new_node.next = self.head # New node ka next = current head
            self.head.prev = new_node  # Old head ka previous = new node
            self.head = new_node     # Head ko update karo
        print(data, "added at beginning")

    def append(self, data):
        new_node = Node(data)  # Naya node create
        if self.head is None:  # Agar list empty hai
            self.head = new_node  # Head ko new node bana do
            print(data, "added at end")
            return

        temp = self.head  # Traversal ke liye temp
        while temp.next is not None: # Last node tak jao
            temp = temp.next
        temp.next = new_node # Last node ka next = new node
        new_node.prev = temp  # New node ka previous = old last node
        print(data, "added at end")

    def count(self):
        # Agar list empty
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp: # Har node visit karo
            count += 1  # Count badhao
            temp = temp.next   # Next node pe jao
        return count

    def insert_at_any_position(self, data):
        new_node = Node(data)  # New node create
        pos = int(input("Enter position: ")) # User se position lo

        # Invalid position check
        # Negative position ya size se badi position allowed nahi
        if pos < 0 or pos > self.count():
            print("Invalid Position")
            return

        elif pos == 0: # Position 0 matlab beginning insertion
            new_node.next = self.head  # New node ka next = current head
            if self.head is not None:  # Agar list empty nahi hai
                self.head.prev = new_node  # Old head ka previous = new node
            self.head = new_node   # Head update
            print(data, "added at", pos)
            return
        else:
            temp = self.head  # Traversal start
            for i in range(pos - 1): # Position se ek node pehle tak jao
                temp = temp.next

            #  CONNECTIONS CHANGE
            new_node.next = temp.next  # New node ka next = current node ke next pe point karega
            new_node.prev = temp  # New node ka prev = current node pe point karega

                # do nodes ke beechme insert karne ka logic
            if temp.next is not None:  # Agar new node last pe nahi insert ho raha
                temp.next.prev = new_node # Next node ka prev = new node pe point karega
            temp.next = new_node # Current node ka next = new node
            print(data, "added at", pos)

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
            print(temp.data, '->', end=' ')
            temp = temp.next
        print('None')

DL = DoublyLinkedlist()  # OBJECT CREATE
while True:
    print("\n--- DOUBLY LINKED LIST MENU ---")
    print("1. Insertion at beginning")
    print("2. Append")
    print("3. Count")
    print("4. Insert at any position")
    print("5. Delete")
    print("6. Display")
    print("7. Sort")
    print("8. Search")
    print("9. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        DL.insertion_at_front(data=int(input("Enter element: ")))

    elif choice == 2:
        DL.append(data=int(input("Enter element: ")))

    elif choice == 3:
        print("Total elements:", DL.count())

    elif choice == 4:
        DL.insert_at_any_position(data=int(input("Enter element: ")))

    elif choice == 5:
        DL.deletion(data=int(input("Enter element: ")))

    elif choice == 6:
        DL.display()

    elif choice == 7:
        DL.sort()

    elif choice == 8:
        DL.search()

    elif choice == 9:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")