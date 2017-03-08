from sys import stdin, stdout

(n, m) = [int(x) for x in stdin.readline().strip().split()]

(xc, yc) = [int(x) for x in stdin.readline().strip().split()]

k = int(stdin.readline().strip())

ans = 0

for i in range(0, k):
    (dx, dy) = [int(x) for x in stdin.readline().strip().split()]
    d = max(n, m)
    if dx > 0:
        d = min(d, (n-xc)//dx)
    elif dx < 0:
        d = min(d, (xc-1)//(-dx))
    if dy > 0:
        d = min(d, (m-yc)//dy)
    elif dy < 0:
        d = min(d, (yc-1)//(-dy))
    xc += d * dx
    yc += d * dy
    ans += d

print(ans)
