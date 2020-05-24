#Python Code for counting sort from 0-9

class CountingSort:
    
    def countingSort(self, arr, size):

        result = [0]*size

        #initialize count array
        count = [0]*10
        #store the count of each elements in count array
        for i in range(0, size):
            count[arr[i]] += 1

        #counting and storing the cummulative sum
        for i in range(1, 10):
            count[i] += count[i-1]

        # Find the index of each element of the original array in count array
        # place the elements in result array
        i = size-1
        while i >= 0:
            result[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            arr[i] = result[i]

#main function
if __name__ == "__main__":
    Sort = CountingSort()
    
    arr = [int(x) for x in input("Enter the array elements: ").split()]

    Sort.countingSort(arr, len(arr))

    print('Sorted array is: ')
    for i in range(len(arr)):
        print(arr[i], end=' ')