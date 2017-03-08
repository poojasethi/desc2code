import sys

n, p, q = sys.stdin.readline().split(' ')
n = int(n)
q = int(q)
p = int(p)
string = sys.stdin.readline().strip()
length = len(string)
flag = False
for i in xrange(0, length / p + 1):
    tmp = length - i * p
    if tmp % q == 0:
        su = tmp / q
        print i + su
        for k in xrange(i):
            print string[k * p: (k + 1) * p]
        for k in xrange(su):
            print string[i * p + k * q: i * p + (k + 1) * q]
        flag = True
        break
if not flag:
    print -1
