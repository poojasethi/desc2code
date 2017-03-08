from sys import stdin
from collections import deque
def main():
    n, m, k = map(int, stdin.readline().split())
    a = [map(int, stdin.readline().split()) for _ in xrange(n)]
    q = [deque() for _ in xrange(m)]
    maxlen = 0;
    left = 0;
    ans = [0] * m

    for i, x in enumerate(a):
        for j, y in enumerate(x):
            while q[j] and a[q[j][-1]][j] <= y:
                q[j].pop()
            q[j].append(i)

        while True:
            t = 0
            for j in xrange(m):
                if q[j]:
                    t += a[q[j][0]][j]
            if t <= k:
                break
            left = left+1
            for j in xrange(m):
                while q[j] and q[j][0] < left:
                    q[j].popleft()

        if i-left+1 > maxlen:
            maxlen = i-left+1
            ans = [a[q[j][0]][j] for j in xrange(m)]
    print ' '.join(map(str, ans))

main()
