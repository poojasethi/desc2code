T = int(input())

s = map(int, raw_input().split())
s = sorted(s)


c = p = 0

while(sum(s)>=p):
    p += s.pop()
    c += 1
print c
