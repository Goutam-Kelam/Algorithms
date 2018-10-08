"""
    This program implements the Abstract Data Type - STACK using Array
"""

# Import maxsize from sys to return -infinite when stack is empty
from sys import maxsize

# Creating Stack
def CreateStack():
    stack = []
    return stack

# Checking for empty stack
def isEmpty(stack):
    return len(stack) == 0

# Pushing in stack
def push(stack,item):
    stack.append(item)
    return stack

# Poping from stack
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize-1) #-infinity
    return stack.pop()

def display(stack):
	print stack

S = CreateStack()
print "Is stack Empty = ",isEmpty(S)
push(S,31)
push(S,143)
display(S)
pop(S)
display(S)

