#!/usr/bin/python

##
# anagram.py - John Coogan
# Use: python anagram.py 
# Will run on all test inputs and outputs.
##

def test_anagram(filename):
    phrases = [p.rstrip() for p in open(filename).readlines()]
    set0 = sorted([x for x in phrases[0]])
    set1 = sorted([x for x in phrases[1]])
    if set0 == set1:
        return "Anagrams!"
    else:
        return "Not anagrams!"

def test():
    import os
    for f in os.listdir('.'):
        if "input" in f:
            print "%s: %s" % (f, test_anagram(f))
        elif "output" in f:
            print "%s: %s" % (f, open(f).read())

if __name__ == '__main__':
    test()