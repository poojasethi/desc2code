from sys import stdin

n = int(stdin.readline().strip())

print('abcd'*(n//4)+'abcd'[0:n%4])
