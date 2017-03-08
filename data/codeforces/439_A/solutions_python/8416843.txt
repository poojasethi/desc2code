[n, d] = map(int, raw_input().split())
t = map(int, raw_input().split())

left = d - sum(t) - (n-1)*10
if left < 0:
    print -1
else:
    print left//5+(n-1)*2