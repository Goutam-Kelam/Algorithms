'''
    This program demonstrates the Euclid's algorithm
    
    let a>b
    a=bq+r, 0<=r<b
    
'''
    
try:
        a = int(raw_input("\nEnter value of a:\n"))
        b = int(raw_input("\nEnter value of b:\n"))
        
        if(a<0 or b<=0):
            print " \nERROR: Values cant be negative or Value of b cant be zero\n"
            exit(0)
            
        if(a<b):
            print "\nERROR: value of a must be greater than value of b\n"
            exit(1)
        
        print "\nValue of a = " ,a
        print "\nValue of b = ",b,"\n"
        
        q=0
        r=a
        
        while(r>=b):
            q=q+1
            r=r-b
        
        print "\nValue of q = " ,q
        print "\nValue of r = ",r,"\n"
        
except ValueError:
	print ' \nWRONG INPUT : Enter Integer Values only'