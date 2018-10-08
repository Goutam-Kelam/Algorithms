"""


"""

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
            
            
            
    def InOrder(self,pos):
        if pos is not None:
            self.InOrder(pos.left)
            print pos.data
            self.InOrder(pos.right)
    
    def PreOrder(self,pos):
        if pos is not None:
             print pos.data
             self.PreOrder(pos.left)
             self.PreOrder(pos.right)
                    
    def PostOrder(self,pos):
        if pos is not None:
            self.PostOrder(pos.left)
            self.PostOrder(pos.right)
            print pos.data
        
        

try:
    print "\nEnter the inputs to create a BST\n"
    arr = [int(x) for x in raw_input().split()]
    print "\nINPUT -\n"
    print arr,"\n\n"
    root = Node(arr[0])
    for i in range(1,len(arr)):
        node = Node(arr[i])
        root.Insert(node)
   
    print "\n\nInorder Traversal -"
    root.InOrder(root)
    print "\n\nPreorder Traversal -"
    root.PreOrder(root)
    print "\n\nPostorder Traversal -"
    root.PostOrder(root)
    
    
except ValueError:
    print "\nERROR: Invalid Input\n"