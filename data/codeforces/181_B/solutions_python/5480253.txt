s, n = 0, int(raw_input())
a = [0] * n
for i in range(n):
    x, y = map(int, raw_input().split())
    a[i] = 10000 * (x + 1000) + y + 1000
a.sort()
b = set(2 * k for k in a)
for i, u in enumerate(a, 2):        
    for v in a[i: ]:
        if v + u in b: s += 1 
print(s)