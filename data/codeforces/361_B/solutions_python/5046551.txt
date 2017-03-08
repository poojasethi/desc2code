import sys

n, k = map(int, raw_input().split(' '))
if n == k:
    print -1
    sys.exit(0)

first = list(range(2, n-k+1))
first.append(1)
first += (list(range(n-k+1, n+1)))

print ' '.join(map(str, first))
