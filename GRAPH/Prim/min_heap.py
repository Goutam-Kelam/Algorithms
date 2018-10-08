 #Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] > arr[l]:
        #smallest=l
        smallest = l
    else:
        smallest = i
    # See if right child of root exists and is
    # greater than root
    #if r < n and arr[smallest] < arr[r]:
        #smallest = r
        
    if r < n and arr[smallest] > arr[r]:
        smallest = r
 
 
    # Change root, if needed
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, smallest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

def Enqueue(arr,n,element):
    arr.append(element)
    n=n+1
    if n>1:
        for i in range(n, -1, -1):
            heapify(arr, n, i)
    return n

def Dequeue(arr,n):
    element = arr[0]
    arr.pop(0)
    n = n-1
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    return (element,n)

def belongTo(arr,element):
    if element in arr:
        return 1
    else:
        return 0
    

 
try:
    print "\nEnter the unsorted integer valued array\n"
    arr = [ int(x) for x in raw_input().split()]
    
    heapSort(arr)
    #n = len(arr)
    print ("\nSorted array is\n")
    print arr
    print "\n"

except ValueError:
    print "\nError: Invalid Input\n"
    exit(0)