#Python code to implement the linked list

#class to represent the node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class to represent the Linked list
class SinglyLinkedlist:
    def __init__(self):
        self.head = None

    #function for insert at end
    def InsertAtEnd(self, data):
        if self.head is None:              #if the list is empty
            self.head = Node(data)
        else:                              #if the list is not empty
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    #function for insert from beginning
    def InsertAtBeginning(self, data):
        if self.head is None:         #if the list is empty
            self.head = Node(data)
        else:                             #if the list is not empty
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    #function to insert an element at specific position
    def InsertAtSpecificPosition(self, data):
        pos = int(input('Enter the position where you want to insert the element: '))
        if pos == 0:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        else:
            t = self.head
            i=0
            while i<pos-1:
                t = t.next
                i += 1
            temp = Node(data)
            temp.next = t.next
            t.next = temp

    #function to delete the element from the beginning
    def DeleteFromBeginning(self):
        if self.head is None:
            return
        else:
            temp = self.head
            self.head = self.head.next
            return temp

    #function to delete the element from the end
    def DeleteFromEnd(self):
        if self.head is None:
            return
        else:
            temp = self.head
            second_last_node = self.head
            while temp.next != None:
                second_last_node = temp
                temp = temp.next
            if temp == self.head:
                self.head = None
            else:
                second_last_node.next = None
            return temp

    #function to delete the element from specific position
    def DeleteFromSpecificPosition(self):
        position = int(input('Enter the position: '))
        # If linked list is empty 
        if self.head == None: 
            return 
        temp = self.head                       # Store head node 
        
        if position == 0:                      # If head needs to be removed 
            self.head = temp.next
            temp = None
            return 
         
        for i in range(position -1 ):               # Find previous node of the node to be deleted
            temp = temp.next
            if temp is None: 
                break
        
        if temp is None:                           # If position is more than number of nodes 
            return 
        if temp.next is None: 
            return  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
        # Unlink the node from linked list 
        temp.next = None
        temp.next = next
            
    #function to display the list
    def displayList(self):
        if self.head is None:
            print('List is empty')
        else:
            print('List is: ')
            temp = self.head
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

#main function
if __name__ == "__main__":
    list = SinglyLinkedlist()
    while 1:
        print()
        print('1. Insert at end')
        print('2. Insert at beginning')
        print('3. Insert at specific position')
        print('4. Delete from beginning')
        print('5. Delete from end')
        print('6. Delete from specific position')
        print('7. View the list')
        print('8. Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            data = int(input('Enter the number: '))
            list.InsertAtEnd(data)

        elif choice == 2:
            data = int(input('Enter the number: '))
            list.InsertAtBeginning(data)

        elif choice == 3:
            data = int(input('Enter the number: '))
            list.InsertAtSpecificPosition(data) 

        elif choice == 4:
            item = list.DeleteFromBeginning()
            if item:
                print('Deleted item is: ',item.data)
            else:
                print('List is empty')

        elif choice == 5:
            item  = list.DeleteFromEnd()
            if item:
                print('Deleted item is: ',item.data)
            else:
                print('List is empty')

        elif choice == 6:
            list.DeleteFromSpecificPosition()
            #if item:
            #    print('Deleted item is: ',item.data)

        elif choice == 7:
            list.displayList()

        elif choice == 8:
            exit(0)

        else:
            print('Invalid choice')