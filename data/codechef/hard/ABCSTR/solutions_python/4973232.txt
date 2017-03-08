def abcstr():
    s = raw_input()
    n = len(s)
    if n < 3:
        return 0
    
    A, B, C = ([0 for _ in xrange(n+1)] for _ in xrange(3))
    
    for i in xrange(1, n+1):
        ch = s[i-1]
        A[i] = A[i-1] + 1 if ch == 'A' else A[i-1]
        B[i] = B[i-1] + 1 if ch == 'B' else B[i-1]
        C[i] = C[i-1] + 1 if ch == 'C' else C[i-1]
    #print A, B, C
    
    count = 0
    from collections import Counter
    counter = Counter()
    
    for j in xrange(0, n+1):
        count += counter[(A[j] - B[j], A[j] - C[j])]
        counter[(A[j] - B[j], A[j] - C[j])] += 1
    #print counter
    print count

if __name__ == "__main__":
    abcstr()