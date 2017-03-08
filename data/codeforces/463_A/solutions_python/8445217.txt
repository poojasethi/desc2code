[n, s] = map(int, raw_input().split())

sweet = -1
for i in range(1, n+1):
    [x, y] = map(int, raw_input().split())
    temp = s*100 - x*100 - y
    if temp >= 0:
        temp = temp % 100
        if temp >= sweet:
            sweet = temp


print sweet
