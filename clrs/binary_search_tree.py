#!/usr/bin/python
# Binary Search Tree

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.p = None
        self.key = val

def tree_insert(T,z):
    y = None
    x = T
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y

    if y == None:
        T = z # Tree T is empty
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print x.key
        inorder_tree_walk(x.right)

def tree_search(x,k):
    if x == None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left,k)
    else:
        return tree_search(x.right,k)

def iterative_tree_search(x,k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x

def tree_succesor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    
    while y != None and x == y.right:
        x = y
        y = y.p
    return y

def transplant(T,u,v):
    if u.p == None:
        T = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    if v != None:
        v.p = u.p

def tree_delete(T,z):
    if z.left == None:
        transplant(T,z,z.right)
    elif z.right == None:
        transplant(T,z,z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T,y,y.right)
            y.right = z.right
            y.right.p = y
        transplant(T,z,y)
        y.left = z.left
        y.left.p = y

#Exercises
#12.2-2
def recursive_tree_minimum(x):
    if x.left == None:
        return x
    else:
        return recursive_tree_minimum(x.left)

def recursive_tree_maximum(x):
    if x.right == None:
        return x
    else:
        return recursive_tree_maximum(x.right)

# 12.2-3
def tree_predecessor(x):
    if x.left != None:
        return tree_maximum(x.left)
    y = x.p
    while y != None and y.left == x:
        x = y
        y = y.p
    return y

T = Node(5)
n1 = Node(3)
n2 = Node(7)
n3 = Node(12)
n4 = Node(6)

tree_insert(T,n1)
tree_insert(T,n2)
tree_insert(T,n3)
tree_insert(T,n4)

inorder_tree_walk(T)

a = tree_succesor(n1)
b = tree_predecessor(n2)

print a.key
print b.key