#!/usr/bin/python
# Longest Common subsequence

def LCS(x, y):
    m = len(x)
    n = len(y)
    C = [[0] * (n + 1) for _ in xrange(m + 1)]
    P = [[0] * (n + 1) for _ in xrange(m + 1)]
    for i in range (1, m + 1):
        for j in range (1, n + 1):
            if (x[i - 1] == y[j - 1]):
                C[i][j] = C[i - 1][j - 1] + 1
                P[i][j] = 1 # mark it
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    # reconstruct
    S = []
    i = m
    j = n

    while(i > 0 and j > 0):
            if (P[i][j] == 1):
                assert (x[i - 1] == y[j - 1])
                S.append(x[i - 1])
                i = i - 1
                j = j - 1
            else:
                if (C[i - 1][j] >= C[i][j - 1]):
                    i = i - 1
                else:
                    j = j - 1
    S.reverse()
    return S

print "LCS: %s" % LCS("This is a test", "I am a test")
