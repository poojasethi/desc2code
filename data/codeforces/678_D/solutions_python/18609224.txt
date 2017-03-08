import sys

MAXN = 10 ** 9 + 7
f = sys.stdin
A, B, n, x = map(int, f.readline().strip().split(' '))
if A == 1:
    print((x + n * B) % MAXN)
else:
    ans = x
    while n > 0:
        if n % 2:
            ans = (A * ans + B) % MAXN;
        B = B * (A + 1) % MAXN;
        A = A * A % MAXN;
        n /= 2
    print(ans)
