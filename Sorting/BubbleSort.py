#Python code for bubble sort

class BubbleSort:

    def bubblesort(self, arr, size):
        
        for Round in range(size):
            flag = 0
            for i in range(size-1-Round):
                if arr[i] > arr[i+1]:
                    flag = 1
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            
            if flag == 0:
                return


if __name__ == "__main__":

    Sort = BubbleSort()
    
    arr = []
    size = int(input('Enter the size of the array: '))

    for i in range(size):
        i += 1
        x = int(input('Enter element %d: '  %i))
        arr.append(x)

    Sort.bubblesort(arr, size)

    print('Sorted array is: ')
    for i in range(size):
        print(arr[i], end=' ')
