# This program gives the output of the following series 
# S = 1+3+5+...+(2n-1)

#raw_input takes the input from user as string
#int() converts it in to integer values - 
# this take cares of boundary conditions such as - input is floating point number or character



# i: number of terms added
		# i = 0, because no terms are added at the starting
		# i will be my loop invariant
# sum : value after adding i terms
		# sum = 0, because 0 terms were added


try:

        print ("\n Enter the number of terms : \t");
	
	n = int(raw_input())
	i = 0 
	sum = 0 

	if n<0:	#BOUNDARY CASE
		print '\nWRONG INPUT :terms cant be negative'
		exit(0)
		"""raise ValueError"""

	if 0==n: #EXCEPTION CASE
		print ' \nNo terms to add\n'
		exit(1)

	if n==1: # ALTERNATIVE CASE
		print '\nthe sum of 1st term is 1\n'
		exit(2)

	while (i!=n):  #NORMAL CASE		# Termination Condition : if i = n, then n terms are already added so we exit the loop
		sum = sum+(2*i+1)
		i = i+1;
	
	
	print '\nthe sum of', n , 'terms is ', sum ,'\n'	

except ValueError:
	print ' \nWRONG INPUT : Enter Integer Values only'
