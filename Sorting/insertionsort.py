#Python code for sorting the array element by insertion sort

class InsertionSort:

    def insertionsort(self, arr, size):
        i = 1

        for i in range(size):
            temp = arr[i]
            j = i-1

            while j>=0 and temp<arr[j]:
                arr[j+1] = arr[j]

                j = j-1
            
            arr[j+1] = temp

if __name__ == "__main__":
    Sort = InsertionSort()
    
    arr = []
    size = int(input('Enter the size of the array: '))

    for i in range(size):
        i += 1
        x = int(input('Enter element %d: '  %i))
        arr.append(x)

    Sort.insertionsort(arr, size)

    print('Sorted array is: ')
    for i in range(size):
        print(arr[i], end=' ')