from sys import stdin

s = list(stdin.readline().strip())

c = max(s)

print(c * s.count(c))
