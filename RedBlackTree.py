
RED = " RED"
BLACK = "BLACK"
NIL = None

class Node:
    def __init__(self,data):
        self.data = data
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None
        
class RedBlackTree:
    def __init__(self):
        self.root = None
        
    def Left_Rotate(self,x):
        y = x.right                     
        x.right = y.left            
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y                  
        
    
    def Right_Rotate(self,x):
        y = x.left    
        x.left = y.right       
        if y.right != NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y               
        
        
    
    def RB_Insert_Fixup(self,z):
        
        while z.parent is not None and z.parent.color == RED:
            if z.parent.parent is not None:
                if  z.parent == z.parent.parent.left:
                    y = z.parent.parent.right
                    if y is not None and y.color == RED:
                        z.parent.color = BLACK
                        y.color = BLACK
                        z.parent.parent.color = RED
                        z = z.parent.parent
                    elif z == z.parent.right:
                        z = z.parent
                        self.Left_Rotate(z)
                    
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                else:
                    y = z.parent.parent.left
                    if y is not None and y.color == RED:
                        z.parent.color = BLACK
                        y.color = BLACK
                        z.parent.parent.color = RED
                        z = z.parent.parent
                    elif z == z.parent.left:
                        z = z.parent
                        self.Right_Rotate(z)
                    
                    z.parent.color = BLACK
                    if z.parent.parent is not None:
                        z.parent.parent.color = RED
        self.root.color = BLACK
            
        
    def RB_Insert(self,z):
        y = NIL
        x = self.root
        while x is not NIL:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == NIL:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
            
        z.left = NIL
        z.right = NIL
        z.color = RED
        self.RB_Insert_Fixup(z)
    
    
    def Tree_Minimum(self,x):
        if x is not NIL:
            while x.left is not NIL:
                x = x.left
            return x
    
    def RB_Transplant(self,u,v):
        if u.parent == NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    """    
    def RB_Delete_Fixup(self,x):
        if x is NIL:
            return
        while x is not self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.colr = RED
                    self.Left_Rotate(x.parent)
                    w = x.parent.right
                
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                elif w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    self.Right_Rotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = BLACK
                w.right.color = BLACK
                self.Left_Rotate(x.parent)
                x = self.root
            else:    
                w = x.parent.left
                    if w.color == RED:
                        w.color = BLACK
                        x.parent.color = RED
                        self.Right_Rotate(x.parent)
                        w = x.parent.left
                    if w.right.color == BLACK and w.left.color == BLACK:
                        w.color = RED
                        x = x.parent
                    elif w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.Left_Rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.RightRotate(x.parent)
                    x = self.root
        x.color = BLACK
        
    def RB_Delete(self,z):
        if y is NIL:
            return
        y = z
        y_original_color = y.color
        if z.left == NIL:
            x = z.right
            self.RB_Delete(z,z.right)
        elif z.right == NIL:
            x = z.left
            self.RB_Delete(z,z.left)
        else:
            y = self.Tree_Minimum(z.right):
            y_original_color = y.color
            x = y.right
            if x is not NIL and y.parent == z:
                x.parent = y
            else:
                self.RB_Transplant(y,y.right)
                y.right = z.right
                if y.right is NIL:
                    return
                y.right.parent = y
            self.RB_Transplant(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.RB_Delete_Fixup(x)
                    
    """
        
        
     
    def Display(self,root):
        if root is not None:
            self.Display(root.left)
            print root.data,"-", root.color,"\n"
            self.Display(root.right)
        

print "\nEnter the nodes to be inserted\n"        
A = [int(x) for x in raw_input().split()]
tree = RedBlackTree()
print "\n--------------------- INSERTION---------------------------\n"
root = Node(A[0])
tree.RB_Insert(root)
for i in range(1,len(A)):
    tree.RB_Insert(Node(A[i]))
    
tree.Display(tree.root)  

print "\n--------------------- DELETE-----------------------------\n"
element = int(raw_input("\n Enter element to delete\n"))
#tree.RB_Delete(element)
#tree.Display(tree.root)
        
        
        
        
        
        
        
        
        
        
