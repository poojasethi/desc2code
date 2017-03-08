from bisect import *

n, m = map(int, raw_input().split())

a = map(int, raw_input().split())
b = map(int, raw_input().split())

a.sort()

for i in b:
    x = bisect_right (a, i)
    print x,
