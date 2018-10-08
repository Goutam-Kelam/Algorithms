"""
    This program implements stack using linkedlist
"""


# class to represent node
class StackNode:
    # constructor to initialize a node
    def __init__(self,data):
        self.data = data
        self.next = None  #python uses None instead of NULL
        
class Stack:
    # constructor to initialize root of linkedlist
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        if self.root is None:
            print "-----------------------STACK EMPTY"
            return True
        else:
            return False
    
    
    def push(self,data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print "%d pushed to stack" %(data)
        
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
	print "%d poped from stack"%(popped)
        return popped
    
    def top(self):
        if (self.isEmpty()):
            return float("-inf")
        print "top of stack - %d"%(self.root.data)
        return self.root.data
    

try:
    print "\n--------STACK---------\n"
    S = Stack()
    done = 1
    while(done):
        print "\n1.Push\n"
        print "2.Pop\n"
        print "3.IsEmpty\n"
        print "4.Top\n"
        choice = int(raw_input("\nEnter your choice- "))
        if choice == 1:
            data = int(raw_input("\nEnter your data- "))
            S.push(data)
        if choice == 2:
            S.pop()
        if choice == 3:
            S.isEmpty()
        if choice == 4:
            S.top()
        done = int(raw_input("\n Are you done- 0.Yes 1.No \n"))
except ValueError:
    print "\nERROR: Enter Valid Inputs\n" 
    

    
