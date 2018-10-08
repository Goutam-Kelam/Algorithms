""""
    This program is to validate the Birthday Paradox
    
"""
from math import *

try:
    print "\nThis program tells you the minimum number of people required to make the probabilty suggestd by you such that 2 people have bday on same day\n"

#    no_of_ppl =0

    desired_prob = float(raw_input("\n\nEnter your desired probability\n"))
    
    if(desired_prob == 100):  #if not taken care, ERROR: Division by Zero
        print "\nTotal no. of ppl = 367\n"
        exit(0)
        
    desired_prob = desired_prob/100

    no_of_ppl = int(ceil((sqrt(2*365*(log(1/(1-desired_prob)))))))
    
    print "\nTotal no. of ppl =",no_of_ppl,"\n"
    
except ValueError:
    print"\n ERROR: Invalid Input\n"
    exit(0)
    