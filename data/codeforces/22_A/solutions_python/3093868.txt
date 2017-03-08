import sys

n = sys.stdin.readline()

a = sorted({int(x) for x in sys.stdin.readline().strip().split()})

print(a[1] if len(a) > 1 else 'NO')
