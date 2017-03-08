t = raw_input().split(' ')
n = int(t[0])
m = int(t[1])
import sys

for i in xrange(n % m):
    sys.stdout.write(str(n / m + 1) + " ")

for i in xrange(m - n % m):
    sys.stdout.write(str(n / m) + ' ')


