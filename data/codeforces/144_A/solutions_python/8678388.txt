import sys

T = input()

s = [int(i) for i in sys.stdin.readline().split()]

a = s.index(max(s))
b = s[::-1].index(min(s))

print a+b - (a>(T-1-b))
