"""
    Merge Sort
"""



def mergesort_routine(A,l,u):
    if l >= u:
        return 
    m = (l+u)/2     #flooring
    mergesort_routine(A,0,m)    #sorting A[l:m+1]
    mergesort_routine(A,m+1,u)  #sorting A[m+1:u+1]
    
    #merge the sorted arrays A[l:m+1] and A[m+1:u+1]
    
    L = [x for x in A[l:m+1]]
    ##print "L is ",L
    #U = A[m+1:u+1]
    U = [x for x in A[m+1:u+1]]
    ##print "U is ",U
    n1 = len(L)
    n2 = len(U)
       # i is the number of the elements copied from L
       # j is the number of the elements copied from U
    #   Loop invariant: A[0:i+j] is a sorted array comprising of elements from L[0:i] and U[0:j]
    #                   where i in [0:n1] and j in [0:n2]
    # i(j) is the number of the elements copied from L(U)
    # Bound function: i+j
    i = 0
    j = 0
    B = []
    while i<n1 and j<n2:
        if L[i] <= U[j]:
            B.append(L[i])
            i = i+1
        else:
            B.append(U[j])
            j = j+1
    if i == n1:
        while j<n2:
            B.append(U[j])
            j = j+1
    elif j == n2:
        while i<n1:
            B.append(L[i])
            i = i+1
    #return A
    A[l:u+1] = B
    
    print "The array is ", B
            
def mergesort(A):
    #if not is type(A,list):
        #print "Error: "
        #return
    N = len(A)
    mergesort_routine(A,0,N-1)

print " Enter the array of integers : "
A = [int(x) for x in raw_input().split()]
#print "the array before sorting ",A 
mergesort(A)
