''' 
    This program produces the square of input number without using multiplication
    
    i:= 
    val:= square of i th number
'''

try :
        num = int(raw_input("\n Enter the number\n"))
        
        if(num == 0): # FOR ZERO
            print "\nThe square of 0 is 0\n" 
            exit(1)
        
              
        if (num > 0): #FOR POSITIVE NUMBERS
            i = 1
            val = 1
            while( i != num):
                val = val + i + i + 1
                i = i+1
        
        if (num < 0): # FOR NEGATIVE NUMBERS
            i = -1
            val = 1
            while( i != num):
                val = val - i - i + 1
                i = i-1
        
        print "\n square of ",num," is ",val
        
except ValueError:
    print "\nEnter integer values only\n "