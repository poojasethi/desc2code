n = int(raw_input())
a = map(int, raw_input().split())
mx = max(a)
print max(mx, (n - 2 + sum(a)) / (n - 1))
