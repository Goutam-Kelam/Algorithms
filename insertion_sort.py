"""
    This program implements insertion sort
    
    Loop Invariants
 ----------------------
    i:= index of element to be sorted
    Array A[0:i-1] is always sorted
    
"""

try:
    print "\n Enter the elements in the array\n"
    A = [int(x) for x in raw_input().split()]
    
    size = len(A)
    
    if (size<0):
        print "Size cant be negative\n"
        exit(0)
    if (size==0):
        print "\n No elements to sort\n"
        
    else:
        i=1
        while(i!=size):
            temp = A[i]
            j=i-1
            while j>=0 and A[j]>temp:
                A[j+1] = A[j]
                j=j-1
            A[j+1] = temp
            i=i+1
        
        print "\n The array after performing Insertion sort\n"
        print A
        
except ValueError:
        print "\nERROR: Enter valid inputs\n"
        exit(0)
    