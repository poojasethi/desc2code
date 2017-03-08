import sys
FIN = sys.stdin
FOUT = sys.stdout
a = list(map(int, FIN.readline().split()))
ans = 0
for i in range(1, len(a)):
    ans += a[i] * i

FOUT.write(str(ans))
