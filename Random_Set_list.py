""" 
    This program implements randomizing the set according to the priorities generated here we will generate another list.
"""
import random 
try:
    print "\n Enter the array of integer numbers\n"
    A = [int(x) for x in raw_input().split()]
    size = len(A)
  #  print size
    print "\n Input Array\n" ,A,"\n"
    
    priority_list = list()
    
    i=0
    while i<size:
        priority_list.append(random.randint(0,pow(size,3)))
        i = i+1
    print "\n The priority list generated\n",priority_list,"\n"
    
    print "\n Array after Sorting wrt Priority list\n"
    
    B = []
    
    for i in range(size):
        max_no = max(priority_list)
        max_index = priority_list.index(max_no)
        B.append(A[max_index])
        priority_list[max_index] = -999
    
    print B
    
    

except ValueError : 
    print "ERROR: \n Invalid Input\n"
    exit(0)