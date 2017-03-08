import sys
import collections

memo = {}

def f(n):
    if n == 0:
        return 0
    elif n in memo:
        return memo[n]
    elif n % 2 == 0:
        v = f(n / 2)
        memo[n] = v
        return v
    elif n % 2 == 1:
        v = f((n - 1) / 2) + 1
        memo[n] = v
        return v

n = int(raw_input())
arr = map(int, sys.stdin.readline().split())

count = collections.Counter()

for a in arr:
    count[f(a)] += 1

result = 0
for key, v in count.iteritems():
    if v > 1:
        result += v * (v - 1)

print result / 2
