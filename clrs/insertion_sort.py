#!/usr/bin/python
# Insertion Sort

def insertion_sort(A):
    for i in xrange(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A

def insertion_sort_descending(A):
    for i in xrange(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A

arr = [15,3,13,8,5,2,5,9,2,4,13,6,1,3,12,1,10,2,7,6,4]
print "Insertion Sort: %s" % insertion_sort(arr)
print "Insertion Sort (Descending): %s" % insertion_sort_descending(arr)