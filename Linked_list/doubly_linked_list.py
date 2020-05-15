#Python code for doubly linked list

#class to represent the node for doubly linked list
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

#class to represent the doubly linked list
class DoublyLinkedlist:
    def __init__(self):
        self.start = None
    
    def InsertAtStart(self, data):
        if self.start is None:
            temp = Node(data)
            self.start = temp
        else:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp

    def InsertAtEnd(self, data):
        if self.start is None:
            temp = Node(data)
            self.start = temp
        else:
            t = self.start
            while t.next is not None:
                t = t.next
            temp = Node(data)
            t.next = temp
            temp.prev = t

    def InsertAfterItem(self, value, data):
        if self.start is None:
            print('List is empty')
            return
        else:
            t = self.start
            while t is not None:
                if t.data == value:
                    break
                t = t.next
            if t is None:
                print('Item not found in the list so value cannot be inserted after that')
            else:
                temp = Node(data)
                temp.prev = t
                temp.next = t.next
                if t.next is not None:
                    t.next.prev = temp
                t.next = temp

    def DeleteFromStart(self):
        #if the list will be empty
        if self.start is None:
            print('List is empty')
            return
        #if the list has only one item 
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def DeleteFromEnd(self):
        #if the list is empty
        if self.start is None:
            print('List is empty')
            return
        #if the list has only one item 
        if self.start.next is None:
            self.start = None
            return
        #going to the last to delete that item 
        t = self.start
        while t.next is not None:
            t = t.next
        t.prev.next = None

    def DeleteByValue(self, item):
        #if the list is empty
        if self.start is None:            
            print('List is empty')
            return
        #if the list has only one item 
        if self.start.next is None:      
            if self.start.data == item:
                self.start = None
                return
            else:
                print('Item not found')
            return
        #if the item will found at the first position
        if self.start.data == item:       
            self.start = self.start.next
            self.start.prev = None
            return
        t = self.start
        #if the element will present at last position in the list
        while t.next is not None:
            if t.data == item:
                break
            t = t.next
        if t.next is not None:
            t.prev.next = t.next
            t.next.prev = t.prev
        else:
            if t.data == item:
                t.prev.next = None
            else:
                print('Item not found')
    
    def displayList(self):
        if self.start is None:
            print('List is empty')
        else:
            t = self.start
            while t is not None:
                print(t.data, end=' ')
                t = t.next

if __name__ == "__main__":
    list = DoublyLinkedlist()

    while 1:
        print()
        print('1. Insert at start')
        print('2. Insert at end')
        print('3. Insert after an item')
        print('4. Delete from start')
        print('5. Delete from end')
        print('6. Delete element by value')
        print('7. Display list')
        print('8. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            data = int(input('Enter the number: '))
            list.InsertAtStart(data)
        elif choice == 2:
            data = int(input('Enter the number: '))
            list.InsertAtEnd(data)
        elif choice == 3:
            value = int(input('Enter the number after you want to insert: '))
            data = int(input('Enter the number: '))
            list.InsertAfterItem(value, data)
        elif choice == 4:
            list.DeleteFromStart()
        elif choice == 5:
            list.DeleteFromEnd()
        elif choice == 6:
            item = int(input('Enter the number which you want to delete: '))
            list.DeleteByValue(item)
        elif choice == 7:
            list.displayList()
        elif choice == 8:
            exit(0)
        else:
            print('Invalid choice')
