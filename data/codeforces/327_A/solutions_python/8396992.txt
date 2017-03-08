n = input()
a = map(int, raw_input().split(" "))
b = [1] * n


for i in range(len(a)):
    if a[i] == 1:
        b[i] = -1
        
c = [b[0]] * n
for i in range(1, n):
    c[i] = max(c[i-1] + b[i], b[i])

print max(c) + sum(a)

