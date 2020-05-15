# Python code for linear search

class LinearSearch:

    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if target == arr[i]:
                return i
        return

if __name__ == "__main__":
    search = LinearSearch()
    arr = []
    size = int(input('Enter the size of the array: '))
    for i in range(size):
        num = int(input('Enter the number %d: ' %i))
        arr.append(num)

    target = int(input('Enter the element you want to search: '))

    index = search.linearSearch(arr, target)
    if index:
        print('Element is present at index ',index)
    else:
        print('Search Unsuccessful')