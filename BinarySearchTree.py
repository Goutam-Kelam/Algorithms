""" 
    This program implements the Binary Search Tree
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
               
        
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
            
            
    def Search(self,data):
        if data == self.data:
            return self
        elif data < self.data:
            if self.left is None:
                return None
            return self.left.Search(data)
        elif data > self.data:
            if self.right is None:
                return None
            return self.right.Search(data)
        else:
            return  None

    def Successor(self):
        successor = None                
        if self:
            if self.right:
                successor = self.right
                while successor.left:
                    successor = successor.left
        return successor
    
    def MinElement(self):  
        if self:
            node = self.left
            if node:
                while node.left:
                    node = node.left
        return node.data
    
    def MaxElement(self):
        if self:
            node = self.right
            if node:
                while node.right:
                    node = node.right
        return node.data
    

    def child_count(self): # To count the number of childerns of a node ... Helpful in Deletion of the node
        count = 0
        if self.left:
            count+= 1
        if self.right:
            count+= 1
        return count



    def Deletion(self,data):
        key = self.Search(data)
        if key is not None:
            no_child = key.child_count()        
        
                   
        if no_child == 0:
            if key.parent:
                if key.parent.left is key:
                    key.parent.left = None
                else:
                    node.parent.right = None
                    del node
            else:
                self.data = None
       
        elif no_child == 1:
            if key.left:
                pos = key.left
            else:
                pos = key.right
            if key.parent:
                if key.parent.left is node:
                    key.parent.left = pos
                else:
                    key.parent.right = pos
                del key
            else:
                self.left = pos.left
                self.right = pos.right
                self.data = pos.data
                self.parent = None
                
        else:  
            successor = key.right
            while successor.left:
                successor = successor.left
            parent = successor.parent
            node.data = successor.data 
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
            del successor
    
    
    
    def display(self):
        if self.left:
            self.left.display()
            print self.data,
        if self.right:
            self.right.display()
        if self.child_count() == 0:
            print self.data,
            
try:
    print "enter elements to enter in the tree: "
    arr = [int(x) for x in raw_input().split()]
    root = Node(arr[0])
    for i in range(1,len(arr)):
        node = Node(arr[i])
        root.Insert(node)
        
    done = 1
    while(done):
        print "\n1.Minimum Element\n"
        print "2.Maximum Element\n"
        print "3.Successor of node\n"
        print "4.No. of children\n"
        print "5.Search an item\n"
        print "6.Delete an item\n"
        print "7.Display Tree\n"
        
        choice = int(raw_input("\nEnter your choice- "))
        if choice == 1:
            print root.MinElement()
        if choice == 2:
            print root.MaxElement()
        if  choice == 3:
            suc = root.Successor()
            if suc is None:
                print "\n No Successor\n"
            else:
                print suc.data
        if choice == 4:
            print root.no_child()
        if choice == 5:
            data = int(raw_input("enter data to be Searched\n"))
            ans=root.Search(data)
            if ans is None:
                print "NO ELEMENT"
            else:
                print "%d is present in Tree"%(ans.data)
        if choice == 6:
            data = int(raw_input("enter data to be Deleted\n"))
            root.Deletion(data)
        if choice == 7:
            root.display()
        
        done = int(raw_input("\n Are you done- 0.Yes 1.No \n"))
                
            
    
    
except ValueError:
    print "\nERROR: Invalid Input\n"