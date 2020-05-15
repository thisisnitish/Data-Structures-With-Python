#Python code for queue implementation using Array

class ArrayQueue:
    
    #initialzing the variables
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.Queue = [None]*capacity

    #function to check the queue is empty or not
    def isEmpty(self):
        return self.front == -1

    #function to check the stack is full or not
    def isFull(self):
        return (self.rear+1) % self.capacity == self.front

    #function to insert the item to the queue
    def enQueue(self, data):
        if self.isFull():           #if the queue will be full
            print('Overflow')
            return
        else:                         #if the queue will not be full
            self.rear = (self.rear+1) % self.capacity           #increase the rear value by 1 and then insert data to the queue
            self.Queue[self.rear] = data
            #check if initially the queue will be empty then increase the value of front
            if self.front == -1:
                self.front = self.rear

    #function to delete the element the from the queue
    def deQueue(self):
        if self.isEmpty():
            print('Underflow')
            return
        else:
            data = self.Queue[self.front]
            #check if there was only one element in the queue
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front+1) % self.capacity
        return data

    #access the front element from the queue
    def queue_front(self):
        if self.isEmpty():
            print('Underflow')
        else:
            print('Front element is: ',self.Queue[self.front])

    #access the rear element from the queue
    def queue_rear(self):
        if self.isEmpty():
            print('Underflow')
        else:
            print('Rear element is: ',self.Queue[self.rear])

    #function to display the queue
    def display_queue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            print('Queue is: ')
            i = self.front
            while i <= self.rear:
                print(self.Queue[i],end=' ')
                i += 1

#main function
if __name__ == "__main__":
    capacity = int(input('Enter the size of the Queue: '))
    #creating the object of the class ArrayQueue
    q = ArrayQueue(capacity)

    while 1:
        print()
        print('1.Enqueue Element')
        print('2.Dequeue Element')
        print('3.Display the Queue')
        print('4.Access the front element')
        print('5.Access the rear element')
        print('6.Exit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            data = int(input('Enter the number: '))
            q.enQueue(data)
        elif choice == 2:
            item  = q.deQueue()
            if item is None:
                print('Queue is empty')
            else:
                print('Dequeued item is: ',item)
        elif choice == 3:
            q.display_queue()
        elif choice == 4:
            q.queue_front()
        elif choice == 5:
            q.queue_rear()
        elif choice == 6:
            exit(0)
        else:
            print('Invalid Choice')
        
            