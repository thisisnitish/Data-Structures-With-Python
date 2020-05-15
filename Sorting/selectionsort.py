if __name__ == "__main__":

    arr = []
    size = int(input('Enter the size of the array: '))

    for i in range(size):
        i += 1
        x = int(input('Enter element %d: '  %i))
        arr.append(x)

    print('Sorted array is: ')
    for i in range(size):
        print(arr[i], end=' ')