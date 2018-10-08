''' This program helps in distributing the Diamonds and Emralds in the Necklace between 2 theives..

Notation:- Diamond = 1;
           Emerald = 0;
           
           Total no. of Gems = 2(k1 + k2)
           No. of Diamonds = 2D
           No. of Emralds = 2E
           
Loop Invariant :- 1) Size of window := k1+k2
                  2) position of window := 
                  
Variables :- d:= Total no. of Diamonds
             i:= position of window
'''

try : 
    
    Necklace = []
    
    D = int(raw_input('\n Enter even no. of Diamonds in Necklace \n'))
    E =  int(raw_input('\n Enter even no. of Emralds in Necklace \n'))
             
    if((D%2!=0) and (E%2!=0)):
        print '\n cant divide necklace equally diamond & emrald must be of even no.\n'
        exit(1)
    D = D/2
    E = E/2
    length_of_necklace = 2*(D+E)
    
    print '\n enter the order of diamond and emralds as - Diamond = 1; Emerald = 0;\n'
    
    for i in range(0,length_of_necklace):
        val = int(raw_input())
        if (val ==0 or val ==1):
            Necklace.append(val)
        else:
            print '\n wrong input for diamond & emrald\n'
            exit(2)
    
    i = 0
    diamond_count=0
    window_size = (D+E)
    
    diamond_count = sum(Necklace[i:window_size])
    #print "\n\n\n",diamond_count,"\n"
     
    while(diamond_count != D):
        diamond_count = diamond_count - Necklace[i] + Necklace[i+D+E]
        i = i+1
    
    print "\nThief 1 gets from index", i+1, "till ", i+D+E
    print "\nThief 2 gets the remaining necklace\n"
    
except ValueError:
	print ' \nWRONG INPUT : Enter Integer Values only'