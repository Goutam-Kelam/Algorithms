def partition(A,l,u):
    
    i = l
    j = u
    
    while(i<=j):
       if A[i] <= A[l]:
           i=i+1
       elif A[j]>A[l]:
           j=j-1
       else:
           A[i],A[j] = A[j],A[i]
           i=i+1
           j=j-1
    
    A[l],A[j] = A[j],A[l]
    
    return j

def QuickSort(A,l,u):
    if l<u:
        mid = partition(A,l,u) 
        QuickSort(A,l,mid-1)
        QuickSort(A,mid+1,u)
    

    
try:
    print "\n Enter the integer array\n"
    A = [int(x) for x in raw_input().split()]
    QuickSort(A,0,len(A)-1)
    print "\nThe sorted array\n",A,"\n"
except ValueError:
    print"\n ERROR: Enter only Integer inputs\n"
    