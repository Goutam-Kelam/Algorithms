"""
This program partition the elements based on the 1st element of the array

A: array of elements
i: left most index of the array 
j: right most index of the array
N: number of elements of the array
"""

try:
    
        A = []

        N = int(raw_input('\n Enter no of terms in array\n'))
        
        if N<0:	#BOUNDARY CASE
		print '\nWRONG INPUT :terms cant be negative'
		exit(0)
		"""raise ValueError"""

	if 0==N: #EXCEPTION CASE
		print ' \nNo Array to process\n'
		exit(1)

        print '\n Enter the Numbers\n'

        for i in range(N):
            A.append(int(raw_input()))

        if N==1: # ALTERNATIVE CASE
		print '\nALT \n'
		print(A)
		exit(2)
		
        print("\nInput Array:\n ")
        print(A)
        print("\n\n")
    
        i = 1
        j = N-1

        while(i<=j):
            if A[i] <= A[0]:
                i=i+1
           
            elif A[j]>A[0]:
                j=j-1
           
            else:
                A[i],A[j] = A[j],A[i]
                i=i+1
                j=j-1
            

        A[0],A[j]= A[j],A[0] # To bring the 1st element in center       
        
        print("\nOutput Array:\n")
        print(A)
        print("\n\n")

except ValueError:
	print ' \nWRONG INPUT : Enter Integer Values only'