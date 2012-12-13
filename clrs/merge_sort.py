#!/usr/bin/python
# Mergesort

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in xrange(0,n1):
        L.append(A[p+i])
    for j in xrange(0,n2):
        R.append(A[q+j+1])

    L.append(None)
    R.append(None)

    i = j = 0

    for k in range(p,r+1):
        if L[i] == None and R[j] != None:
            A[k] = R[j]
            j = j + 1
        elif R[j] == None and L[i] != None:
            A[k] = L[i]
            i = i + 1
        else:        
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1

def merge_sort(A,p,r):
    if p < r:
        q = (p + r)/2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

arr = [15,3,13,8,5,2,5,9,2,4,13,6,1,3,12,1,10,2,7,6,4]
merge_sort(arr, 0, 20)
print "Mergesort: %s" % arr