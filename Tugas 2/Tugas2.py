# Node class definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insert node
def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value <= root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

#pre-order tree traversal
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# in-order tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

#  post-order tree traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# Main program
def main():
    root = None

    while True:
        print("\nBinary Tree Creation and Traversal Program")
        print("1. Tambah Data atau node")
        print("2. Pre-order traversal")
        print("3. In-order traversal")
        print("4. Post-order traversal")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # pilih = 2
            # while pilih == 1:
                value = input("Masukkan data: ")
                root = insert(root, value)
                # pilih = input("nambah lagi ? 1/2 ")
        elif choice == 2:
            print("\nPre-order Traversal:")
            preorder(root)
            print()
        elif choice == 3:
            print("\nIn-order Traversal:")
            inorder(root)
            print()
        elif choice == 4:
            print("\nPost-order Traversal:")
            postorder(root)
            print()
        elif choice == 5:
            break
        else:
            print("isi yang bener oi.")

if __name__ == "__main__":
    main()
