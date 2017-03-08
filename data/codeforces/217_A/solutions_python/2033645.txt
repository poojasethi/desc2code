p = []

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(i, j):
    a = find_set(i)
    b = find_set(j)
    p[a] = b

n = input()
pl = []
for i in range(n):
    v = raw_input().split()
    pl.append(v)

#make set
for i in range(n):
    p.append(i)   #p[x] = x

for i in range(n):
    for j in range(i+1, n):
        if pl[i][0] == pl[j][0] or pl[i][1] == pl[j][1]:
            union(i, j)

s = set()
for i in range(n):
    s.add(find_set(i))

print len(s) - 1
