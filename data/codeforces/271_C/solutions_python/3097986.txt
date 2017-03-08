from sys import stdin

(n, k) = [int(x) for x in stdin.readline().strip().split()]

if n // k < 3:
    print('-1')
else:
    ans = sorted((list(range(1,k+1))*(n//k))[0:n-k])+list(range(1,k+1))
    print(' '.join([str(x) for x in ans]))
