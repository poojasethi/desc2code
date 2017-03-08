n = int(raw_input())
l = []
for i in range(n):
    s = raw_input()
    l.append(s)
l_u = set(l)
maxi = 1
for e in l_u :
    maxi = max(maxi, l.count(e))
print maxi