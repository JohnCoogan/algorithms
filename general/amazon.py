#!/usr/bin/python
# An Amazon interview questions

from heapq import heapify, heappushpop
from math import hypot
from random import random

def nsmallest(xypoints, n):
    """Use a heap with the maximum of the n lowest at the top of the heap"""
    # first fill the heap with the first n points
    heap = [(-hypot(x, y), (x, y)) for x, y in xypoints[:n]]
    heapify(heap)
    # now push new elements on heap only if distance small enough
    for x, y in xypoints[n:]:
        dist = hypot(x, y)
        if dist < -heap[0][0]:
            heappushpop(heap, (-dist, (x, y))) # remove "worst"
    return heap

data = [(random() * 1000, random() * 1000) for x in range(1000)]
smallest = nsmallest(data, 10)
print smallest