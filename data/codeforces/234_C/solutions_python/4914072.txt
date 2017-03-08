import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(sys.stdin.readline()) - 2
t = [int(x) for x in sys.stdin.readline().split()]
s = int(t[0] >= 0) + int(t[-1] <= 0)
if n:
    t, p = t[1: -1], [0] * n

    x = 0
    for i in range(n):
        if t[i] < 0: x += 1
        p[i] = x
    t.reverse()
    p.reverse()

    x = 0
    for i in range(n):
        if t[i] > 0: x += 1
        p[i] += x

    print(s + n - max(p))
else: print(s)
