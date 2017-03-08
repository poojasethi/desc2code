n, x = map(int,raw_input().split(" "))
arr = map(int,raw_input().split(" "))
arr.sort()

ans = 0
for i in arr:
    ans += x * i
    if x > 1: x -= 1
print ans
