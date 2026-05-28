class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Note: Recursive calls ke baad return karna padta hai taki tree updated rahe
    def insert(self,root,data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left,data)  # recursive function

        elif data > root.data:
            root.right = self.insert(root.right,data)   # recursive function
        return root

    def search(self,root,key):
        if root is None:
            return False
        if key == root.data:
            return True
        elif key < root.data:
            return self.search(root.left,key)  # recursive function
        else:
            return self.search(root.right,key)  # recursive function

#      Find Minimum value used in delete function
    def find_min(self,root):
        while root.left is not None:  #     jab tak aur left available hai, tab tak left jao
            root = root.left
        return root

    def delete(self,root,key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left,key)   # recursive function

        elif key > root.data:
            root.right = self.delete(root.right,key)   # recursive function

        else:
#             agar ek child ya 0 child hai
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

#         agar node ke 2 child hai
                temp = self.find_min(root.right)
                root.data = temp.data
                root.right = self.delete(root.right,temp.data)  # recursive function
        return root

#     Traversals
    def InorderTraversal(self,root):
        if root:
            self.InorderTraversal(root.left)
            print(root.data)
            self.InorderTraversal(root.right)

    def PreOrderTraversal(self,root):
        if root:
            print(root.data)
            self.PreOrderTraversal(root.left)
            self.PreOrderTraversal(root.right)

    def PostOrderTraversal(self,root):
        if root:
            self.PostOrderTraversal(root.left)
            self.PostOrderTraversal(root.right)
            print(root.data)

    # -------- MENU DRIVEN PART --------
bst = BinarySearchTree()

while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        bst.root = bst.insert(bst.root, val)
        print("Node inserted")

    elif choice == 2:
        val = int(input("Enter value to delete: "))
        bst.root = bst.delete(bst.root, val)
        print("Node deleted (if existed)")

    elif choice == 3:
        val = int(input("Enter value to search: "))
        if bst.search(bst.root, val):
            print("Value found in tree")
        else:
            print("Value not found")

    elif choice == 4:
        print("Inorder Traversal:")
        bst.InorderTraversal(bst.root)

    elif choice == 5:
        print("Preorder Traversal:")
        bst.PreOrderTraversal(bst.root)

    elif choice == 6:
        print("Postorder Traversal:")
        bst.PostOrderTraversal(bst.root)

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")



