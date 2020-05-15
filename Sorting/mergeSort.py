#Merge Sort implementation in python
class MegreSort:

    def mergesort(self, arr):

        if len(arr) > 1:
            mid = len(arr)//2   #Finding the mid of the array 
            Left = arr[:mid]   #dividing the array into two halves
            Right = arr[mid:]

            #calling the mergesort function for sorting the first and second halves
            self.mergesort(Left)
            self.mergesort(Right)

            i = j = k = 0

            #copy data to temporary arrays Left[] and Right[]
            while i < len(Left) and j < len(Right):
                if Left[i] < Right[j]:
                    arr[k] = Left[i]
                    i += 1
                else:
                    arr[k] = Right[j]
                    j += 1
                k += 1

            #check if any element is left

            while i < len(Left):
                arr[k] = Left[i]
                i += 1
                k += 1
            
            while j < len(Right):
                arr[k] = Right[j]
                j += 1
                k += 1


#main function
if __name__ == "__main__":
    Sort = MegreSort()
    
    arr = []
    size = int(input('Enter the size of the array: '))

    for i in range(size):
        i += 1
        x = int(input('Enter element %d: '  %i))
        arr.append(x)

    Sort.mergesort(arr)

    print('Sorted array is: ')
    for i in range(size):
        print(arr[i], end=' ')