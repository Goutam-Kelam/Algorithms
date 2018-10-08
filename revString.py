'''
    This program reverses a string
    i = index to be swapped from left
    j = index to be swapped from right
    
'''

try:
    
    Str = raw_input("\nEnter the string \n")
    
    input_str = list(Str)
    
    print " \nOriginal String: " ,Str
    
    i = 0
    j = len(Str)-1
    temp = ' '
    while(j>i):
        input_str[i],input_str[j] = input_str[j],input_str[i]
        i = i+1
        j = j-1
        Str = ''.join(input_str)
 #   print w[::-1]   one line code to reverse the string
    
    print " \nReversed String: " ,Str
    
except ValueError:
	print ' \nWRONG INPUT : Enter Character string only'