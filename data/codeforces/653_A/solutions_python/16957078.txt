n = int(raw_input())
sz = [int(i) for i in raw_input().split()]

s = list(set(sz))
s.sort()

# print s
f = False
for i in range(len(s)-2):
    if s[i+1] - s[i] == 1 and s[i+2] - s[i+1] == 1:
        print "YES"
        f = True
        break

if not f:
    print "NO"
