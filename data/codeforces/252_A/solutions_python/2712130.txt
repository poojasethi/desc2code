n = int(raw_input())
s = raw_input().split()
a = [0] + [int(s[i]) for i in range(0, n)]
for i in range(1, n + 1):
    a[i] ^= a[i - 1]
ans = 0
for i in range(1, n + 1):
    for j in range(0, i):
        ans = max(ans, a[i] ^ a[j])
print(ans)
