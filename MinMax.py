""" 
        This program finds the maximum and minimum numbers in an array
        using Divide and Conquer method
"""

def MinMax(A , start , last):
    if (len(A)==1):
        return(A[0],A[0])
    if(len(A) == 2):
        if(A[0]>=A[1]):
            return (A[1],A[0])
        else: return (A[0],A[1])
    
    else:
            lpos = (last+start) / 2
            val1 =  MinMax(A[start:lpos],start,lpos)
            val2 = MinMax(A[lpos+1:],lpos+1,last)
            
            if(val1[0]>=val2[0]):
                trueMin = val2[0]
            else: trueMin = val1[0]
  
            if(val1[1]>=val2[1]):
                trueMax = val1[1]
            else: trueMax = val2[1]

            return(trueMin,trueMax)


try:
    A = list()
    size = int(raw_input("\n Enter the no. of terms you want to input in the array\n"))
    
    if(size<0):
        print "\n Array cant be of negative size\n"
        exit(1)
        
    if(size == 0):
        print "\n No element\n"
        exit(2)
        
    print "\n Enter the elements\n"
    
    for i in range(size):
        A.append(int(raw_input()))
    """ 
    if(len(A) == 1):
        print "\nsingle element array min and max are same:"
        print "Min = Max = ",A[0],"\n"
        exit(0)
   
    start = 0
    last = size-1
    """
    (minEle, maxEle) = MinMax(A,0,size-1)
    
    print "The minimum and maximum elements in the array is ", (minEle, maxEle)
    
except ValueError:
    print "\n Enter Integers only\n"
