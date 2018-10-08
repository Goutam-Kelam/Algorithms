"""
    This program implements the Binary search (Leftmost occurance)
    
"""

def ordertest(A):
    if (len(A) == 1):
        return 0
    else:
        return all(A[i] >= A[i+1] for i in range(len(A)-1))

try:
    print "\n Enter the integer numbers in an sorted array format\n"
    A = [int(x) for x in raw_input().split()]
      
    no_of_element = len(A)
    
    if(no_of_element == 0):
        print "\nNo Elements to search\n"
        exit(0)
    
    check = ordertest(A)
    if(check):
        print"\n input is not sorted\n"
        exit(1)
   
    x = int(raw_input("\n Enter the no. you wanna search\n"))
    
    lower_bound = 0
    upper_bound = no_of_element - 1
    
    while  lower_bound < upper_bound:
        middle = (lower_bound + upper_bound) / 2  #FLOORING
        if(A[middle]>=x):
           upper_bound = middle
        else:
            lower_bound = middle+1
    
    if(A[lower_bound] == x):
        print " \nElement found in Position : ",lower_bound+1,"\n"
    else:
        print "\nElement not found\n"
        
except ValueError:
    print " \nERROR: integer inputs only\n"
    