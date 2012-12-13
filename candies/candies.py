#!/usr/bin/python

##
# candies.py - John Coogan
# Use: python candies.py [0,1,2] to indicate test data.
##

def main(values):
    scores = [int(x) for x in values[1:]]
    candies = [1 for x in scores]
    done = False
    while done == False:
        done = True
        for child in xrange(len(scores)):
            for y in [1,-1]:
                neighbor = child + y
                if neighbor >= 0 and neighbor < len(scores):
                    if scores[neighbor] > scores[child] and candies[neighbor] <= candies[child]:
                        candies[neighbor] = candies[child] + 1
                        done = False
    return sum(candies)

def test():
    import sys
    if len(sys.argv) == 2:
        t = int(sys.argv[1])
        f = "input0%s.txt" % t
        values = [v.rstrip() for v in open(f).readlines()]
        G = main(values)
        print "%s: %s" % (f, G)
        o = "output0%s.txt" % t
        A = int(open(o).read().rstrip())
        print "%s: %s" % (o, A)

if __name__ == '__main__':
    test()