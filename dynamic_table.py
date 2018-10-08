"""
    This program implements the dynamic table using fibbonacci method to get a golden ratio
"""

import math as m
global_Fib_list = []
class Table:
    
    def __init__(self):
        self.num = 0
        self.size = 0
        self.keys = [None for i in range(self.size)]
    
    def get_Fib_num(self,table_size):
        phi = (1+m.sqrt(5))/2
        phi_hat = (1-m.sqrt(5))/2
        pow_phi = m.pow(phi,table_size+2)
        pow_phi_hat = m.pow(phi_hat,table_size+2)
        return int(((pow_phi-pow_phi_hat)/m.sqrt(5)))
    
    
    def makeDouble(self,newsize):
        oldsize = self.size
        oldkeys = self.keys
        self.size = newsize
        self.num = oldsize
        self.keys = [None for i in range(newsize)]
        for i in oldkeys:
            self.keys.append(i)
        return self.keys
    
    def Table_insert(self,x):
        if self.num<self.size:
            self.keys.append(x)
            self.num+=1
        
        else:
            fib_num = self.get_Fib_num(self.size)
            if (self.size == 0 and fib_num ==1) or (self.size == 2 and fib_num == 2):
                self.keys = self.makeDouble(fib_num)
                self.keys[self.num] = x
                self.num+=1
                global_Fib_list.append(self.size)
            else:
                newSize = global_Fib_list[len(global_Fib_list)-1] + global_Fib_list[len(global_Fib_list) -2]
                self.keys = self.makeDouble(newSize)
                self.keys[self.num] = x
                self.num+=1
                global_Fib_list.append(newSize)
        print x,"\t\t",self.num,"\t\t",self.size         
    
    def Table_delete(self):
        
        if(self.num-1 == global_Fib_list[len(global_Fib_list)-2]):
            newSize = global_Fib_list[len(global_Fib_list) - 2]
            self.num -= 1
            self.keys[self.num] = None
            oldkeys = self.keys
            self.size = newSize
            self.num = 0
            self.keys = [None for i in range(newSize)]
            for i in oldkeys:
                self.keys.append(i)
            global_Fib_list.remove(global_Fib_list[len(global_Fib_list)-1])        
        else:
            self.num-=1
            self.keys[self.num]=None
        print x,"\t\t",self.num,"\t\t",self.size     
            
   
    
    
try:
    
    print "\nEnter the elements to insert\n"
    arr = [int(x) for x in raw_input().split()]
    
    print "\n Insertion"
    print "\nArray\tTableEntries\tTableCapacity\n"
    
    t = Table()
    for i in arr:
        t.Table_insert(i)
        
    
    print "\nDELITION"
    print "\nArray\tTableEntries\tTableCapacity\n"
    
    for i in arr:
        t.Table_delete()
        
except ValueError:
    print "\nERROR: Wrong input\n"
    exit(0)
            