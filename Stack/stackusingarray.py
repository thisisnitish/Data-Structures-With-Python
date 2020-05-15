#Python code for stack implementation using Array

class ArrayStack:

    #initializing the stack
    def __init__(self):
        self.stack = []

    #function to return the length of the stack
    def __len__(self):
        return len(self.stack)

    #function to check the stack is empty or not
    def isEmpty(self):
        return len(self.stack) == 0

    #function to push the element in the stack
    def push(self, data):
        self.stack.append(data)

    #function to access the top element from the stack
    def topElement(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            return self.stack[-1]

    #function to pop the element from the stack
    def pop(self):
        if self.isEmpty():
            print('Stack Undeflow')
        else:
            self.stack.pop()

    #function to display the stack
    def displayStack(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print(self.stack)

#main function   
if __name__ == "__main__":

    #creating the object for the class ArrayStack
    a = ArrayStack()

    while 1:
        print('1.Push Element')
        print('2.Pop Element')
        print('3.Display')
        print('4.Top element')
        print('5.Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            data = int(input('Enter the number: '))
            a.push(data)
        elif choice == 2:
            a.pop()
        elif choice == 3:
            a.displayStack()
        elif choice == 4:
            print('Top element is: ',a.topElement())
        elif choice == 5:
            exit(0)
        else:
            print('Invalid Choice')
        