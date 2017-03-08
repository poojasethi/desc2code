from sys import stdin

a = stdin.readline().strip()
b = stdin.readline().strip()
c = stdin.readline().strip()

print('YES' if a == c[::-1] and b == b[::-1] else 'NO')
