#Python code for binary search tree implementation

#A node class to represent a node
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertNode(self, info):
        if self.root is None:
            self.root = Node(info)
        else:
            self.utilityInsert(self.root, info)

    def utilityInsert(self, root, info):
        if info < root.info:
            if root.left is None:
                root.left = Node(info)
            else:
                self.utilityInsert(root.left, info)
        else:
            if root.right is None:
                root.right = Node(info)
            else:
                self.utilityInsert(root.right, info)

#    def deleteNode(self, root, info):
#        if root is None:
#            return 

    def DisplayTree(self, orderChoice):

        if orderChoice == 1:
            self.inOrder(self.root)
        elif orderChoice == 2:
            self.preOrder(self.root)
        elif orderChoice == 3:
            self.postOrder(self.root)
        elif orderChoice == 4:
            exit(0)
        else:
            print('Invalid Choice')

    def inOrder(self, root):
        if root == None:
            return 'Tree is empty'
        t = root
        if t != None:
            self.inOrder(t.left)
            print(t.info, end=' ')
            self.inOrder(t.right)

    def postOrder(self, root):
        if root == None:
            return 'Tree is empty'
        t = root
        if t != None:
            self.preOrder(t.left)
            self.preOrder(t.right)
            print(t.info, end=' ')

    def preOrder(self, root):
        if root == None:
            return 'Tree is empty'
        t = root
        if t != None:
            print(t.info, end=' ')
            self.preOrder(t.left)
            self.preOrder(t.right)


if __name__ == "__main__":
    Tree = BinarySearchTree()

    while 1:
        print()
        print('1. Insert Node')
        print('2. Delete Node')
        print('3. Display Tree')
        print('4. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            info = int(input('Enter the number: '))
            Tree.insertNode(info)

        elif choice == 2:
            print('This function is yet to implement')

        elif choice == 3:
            print()
            print('1. Inorder')
            print('2. Preorder')
            print('3. Postorder')
            print('4. Exit')
            orderChoice = int(input('Enter the choice for traversal: '))
            Tree.DisplayTree(orderChoice)

        elif choice == 4:
            exit(0)

        else:
            print('Invalid Choice')

