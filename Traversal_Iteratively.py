"""
    This program builds the BST &
    prints it using InOrder traversal iteratively
    
    This program uses Stack implemented as Linkedlist 

"""
# class to represent node
class StackNode:
    # constructor to initialize a node
    def __init__(self,data,purpose):
        self.data = data
        self.purpose = purpose
        self.next = None  #python uses None instead of NULL

class Stack_preNode:
    def __init__(self,data):
        self.data = data
        self.next = None 
    
class Stack:
    # constructor to initialize root of linkedlist
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
        
    def push(self,data,purpose):
        newNode = StackNode(data,purpose)
        newNode.next = self.root
        self.root = newNode
        #print "(%d,%d) pushed to stack" %(data)%(purpose)
        
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        purpose = temp.purpose
	#print "(%d,%d) poped from stack"%(popped)%(purpose) 
        return (popped,purpose)
 


class PreStack:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
            
    def push(self,data):
        newNode = Stack_preNode(data)
        newNode.next = self.root
        self.root = newNode
        
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
 

    
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
        
    def Insert(root,node):
        if root is None:
            root = node
        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    root.right.Insert(node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    root.left.Insert(node)
    
    def InOrder(self,pos): # pos gets the root
        new = []
        S = Stack()
        S.push(pos,1)
        while(not S.isEmpty()):
            (ptr,purpose) = S.pop()
            if ptr is not None:
                if purpose:
                    S.push(ptr,0)
                    S.push(ptr.left,1)
                else:# if not purpose
                    new.append(ptr.data)
                    S.push(ptr.right,1)
        return new
        
    def PostOrder(self,pos):
        new = []
        S= Stack()
        S.push(pos,1)
        while not S.isEmpty():
            (ptr,purpose) = S.pop()
            if ptr is not None:
                if purpose:
                    S.push(ptr,0)
                    S.push(ptr.right,1)
                    S.push(ptr.left,1)
                    
                else:
                    new.append(ptr.data)
        return new
                    
                    
    def PreOrder(self,pos):
        new = []
        S = PreStack()
        S.push(pos)
        while not S.isEmpty():
            ptr = S.pop()
            if ptr is not None:
                new.append(ptr.data)
                S.push(ptr.right) # right child is pushed first as we need left child first
                S.push(ptr.left)
        return new
    
            
try:
    print "\nEnter the inputs to create a BST"
    arr = [int(x) for x in raw_input().split()]
    print "\nINPUT -"
    print " ".join(map(str,arr))
    root = Node(arr[0])
    for i in range(1,len(arr)):
        node = Node(arr[i])
        root.Insert(node)
   
    print "\nInorder Traversal (iteratively) -"
    inorder = root.InOrder(root)
    print " ".join(map(str,inorder))
    print "\nPostorder Traversal (iteratively) -"
    postorder = root.PostOrder(root)
    print " ".join(map(str,postorder))
    print "\nPreorder Traversal (iteratively) -"
    preorder = root.PreOrder(root)
    print " ".join(map(str,preorder))
    print "\n\n"
    
except ValueError:
    print "\nERROR: Invalid Input\n"