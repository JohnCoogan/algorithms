#!/usr/bin/python
# Steve Yegge's Phone Interview Questions

# Write a function to reverse a string.
def reverse(string):
    return ''.join([string[len(string)-i-1] for i in range(len(string))])

# Write function to compute Nth fibonacci number.
memo = {0:0, 1:1}
def mfib(n):
    if not n in memo:
        memo[n] = mfib(n-1) + mfib(n-2)
    return memo[n]

# Print out the grade-school multiplication table up to 12x12.
def grade_school(x):
    x += 1
    line = ' ' * 5
    for n in xrange(1,x):
        line += '%5.0f' % n
    print line
    line = '-' * 5 * x
    print line
    for h in xrange(1,x):
        line = '%2.0f | ' % h
        for w in xrange(1,x):
            line += "%5.0f" % (h*w)
        print line

# Write a function that sums up integers from a text file, one int per line.
def int_sum(filename):
    return sum([int(l.rstrip()) for l in open(filename, 'r').readlines()])

# Write function to print the odd numbers from 1 to 99.
def odd_ints(num):
    return [x for x in range(num) if x % 2 == 1]

# Find the largest int value in an int array.
def find_max(arr):
    return max(arr)

def find_max_manual(arr):
    maximum = 0
    for x in arr:
        if x > maximum:
            maximum = x
    return maximum

# Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.
def format_RGB(r,g,b):
    return "%2s%2s%2s" % (hex(r)[2:].upper(), hex(g)[2:].upper(), hex(b)[2:].upper())

if __name__ == '__main__':
    from random import randrange
    print reverse("This is a test!")
    print mfib(100)
    grade_school(12)
    print int_sum("ints.txt")
    print odd_ints(100)
    print find_max_manual([randrange(0,1000) for x in range(100)])
    print format_RGB(randrange(0,255),randrange(0,255),randrange(0,255))