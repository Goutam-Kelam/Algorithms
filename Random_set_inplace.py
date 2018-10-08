""" 
    This program implements randomizing the set according to the priorities generated, here we will use inplace method.
"""
from random import *
try:
 
        print "\n Enter the number of elements you wanna enter\n"
        size = int(raw_input())
        print "\n Enter the integer elements\n"
        A=list()
        for i in range(size):
            A.append(int(raw_input()))
          
        print "\n Input Array\n" ,A,"\n"
    
        #B = []
    
        for i in range(size):
            rand_index = randrange(i,size) # +1 because randrange is closed open
            print "\nRandom Index at iteration ",i,"=",rand_index
            A[i],A[rand_index]=A[rand_index],A[i]
            
            #B.append(A[random.randint(i,size)])
            #A[i] = A[random.randint(i,size)]
        print "\n Array after Sorting wrt Priority list"
        print A,"\n\n"
        #print B
    
    

except ValueError : 
    print "ERROR: \n Invalid Input\n"
    exit(0)