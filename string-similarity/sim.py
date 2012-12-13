#!/usr/bin/python

##
# String Similarity - John Coogan
# Calculates similarity between a string and its suffixes.
##

def test_sim(filename):    
    phrases = [p.rstrip() for p in open(filename).readlines()]
    for p in phrases[1:]:
        counter = 0
        for x in range(len(p)):
            for i,y in enumerate(p[x:]):
                if y == p[i]:
                    counter += 1
                else:
                    break
        print counter

def test():
    import os
    for f in os.listdir('.'):
        if "input" in f:
            test_sim(f)

test()