#!/usr/bin/python

# See how many times prime i goes into N
# Sum of each (multiplicity + 1) will = # of factors
# Double because of formula transformation
def get_multiplicity(i, N):
    duplicate = N
    multiplicity = 0
    while duplicate != 0:
        multiplicity += duplicate / i
        duplicate = duplicate / i
    return (2 * multiplicity + 1)

# result is product of each multiplicity mod 1000007
def compute_num_factors(multiplicities):
    result = 1
    for i in xrange(2, len(multiplicities)):
        if multiplicities[i] != -1:
            result = (result * multiplicities[i]) % 1000007
    return result % 1000007

# Get multiplicities for each prime 
def compute_prime_multiplicity(primes, N):
    multiplicities = [-1 for x in xrange(len(primes))]
    for i in xrange(2,len(primes)):
        if primes[i] == 1:
            multiplicities[i] = get_multiplicity(i, N)
    return compute_num_factors(multiplicities)

# find all primes below N, not necessarily factors
def generate_primes(N):
    primes = [1 for x in xrange(N+1)]
    for i in xrange(2,N):
        if i * i <= N:
            for j in xrange(2,N):
                if j * i <= N:
                    primes[j*i]=0;
                else:
                    break
        else:
            break
    return primes

# Read in number and call calc functions.
def factor(N):
    primes = generate_primes(N)
    answer = compute_prime_multiplicity(primes, N)
    return answer

def test():
    import sys
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        print "%s: %s" % (N, factor(N))
    else:
        import os
        for f in os.listdir('.'):
            if "input" in f:
                N = int(open(f).read().rstrip())
                print "%s: %s" % (f, factor(N))
            if "output" in f:
                A = int(open(f).read().rstrip())
                print "%s: %s" % (f, A)

test()