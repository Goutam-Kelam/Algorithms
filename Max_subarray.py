"""
    This program implements maximum sum subarray problem
"""


def MaxCrossingSum( A, l, m, u):
    Sum = 0
    left_sum = 0
    ITER = m
    
    max_left = l
    max_right = u
    
    while (ITER>=l):
        Sum = Sum + A[ITER]
        if(Sum >=left_sum):
            left_sum = Sum
            max_left = ITER
        ITER =ITER-1
        
    Sum = 0
    right_sum = 0
    ITER = m+1
    
    while(ITER<= u):
        Sum = Sum+A[ITER]
        if(Sum>=right_sum):
            right_sum = Sum
            max_right = ITER
        ITER = ITER+1
        
    return (max_left, max_right, left_sum + right_sum)

def MaxSumSubArray(A,l,u):
    # Base Case ----- ONLY 1 ELEMENT
    if(l==u):
        return (l,u,A[l])
    
    # Finding middle index
    m = (l+u)/2
    
    """ Returns 3 cases -
        1) Max subarray sum in left side
        2) Max subarray sum in right side
        3) Max subarray sum on crossingOver
    """
    (left_low, left_high, left_sum) = MaxSumSubArray(A,l,m)
    (right_low, right_high, right_sum) = MaxSumSubArray(A,m+1,u)
    (cross_low, cross_high,cross_sum) = MaxCrossingSum(A,l,m,u)
    
    if (left_sum>=right_sum and left_sum>=cross_sum):
        return (left_low,left_high,left_sum)
    elif (right_sum>=left_sum and right_sum>=cross_sum):
        return (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)

try:
    print "\n Enter the integer Array\n"
    A = [int(x) for x in raw_input().split()]
    size = len(A)

    if(size == 0):
        print "\n No array\n"
        exit(0)
    
    (max_low,max_high,max_sum) = MaxSumSubArray(A,0,size-1)
    
    print "\n The maximum contiguous sum is" ,max_sum,"\n"
    print "The maximum array is from",max_low+1,"to",max_high+1, "\n"
    
except ValueError:
    print "\nERROR: Enter valid input\n"