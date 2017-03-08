n = input()
a = list(reversed(sorted(map(int, raw_input().split(' ')))))
for i in range(1, n):
    if a[i] >= a[i - 1]:
        a[i] = max(a[i - 1] - 1, 0)
print sum(a)
