#!/usr/bin/python
# Quicksort

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, q):
    from random import randint
    swap(A, p, randint(p, q)) # put a random element at the front
    x = A[p]
    i = p
    for j in xrange(p+1, q+1):
        if A[j] <= x:
            i = i + 1
            swap(A, i, j)
    swap(A, p, i) # put the pivot in its right place
    return i

def quicksort(A, p, q):
    if p < q:
        i = partition(A, p, q)
        quicksort(A, p, i - 1)
        quicksort(A, i + 1, q)

arr = [15,3,13,8,5,2,5,9,2,4,13,6,1,3,12,1,10,2,7,6,4]
quicksort(arr, 0, 20)
print "Quicksort: %s" % arr