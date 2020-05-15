#Python code for binary search

class BinarySearch:

    def binarysearch(self, arr, target, low, upper):
        
        if low <= upper:
            mid = (low + upper)//2

            if target == arr[mid]:
                return 1
            elif target > arr[mid]:
                return self.binarysearch(arr, target, mid+1, upper)
            else:
                return self.binarysearch(arr, target, low, mid-1)


if __name__ == "__main__":
    search = BinarySearch()
    
    arr = []
    size = int(input('Enter the size of the array: '))
    for i in range(size):
        i += 1
        num = int(input('Enter the number %d: ' %i))
        arr.append(num)
    arr.sort()
    target = int(input('Enter the element you want to search: '))
    found = search.binarysearch(arr, target, 0, len(arr)-1)
    
    if found:
        print('Search Successful')
    else:
        print('Search Unsuccessful')