import sys

line = sys.stdin.readline()
n, m = line.strip().split(" ")
n = int(n)
m = int(m)
line = sys.stdin.readline()
f = line.strip().split(" ")
df = {}
dup = set()
idx = 0
for item in f:
    idx += 1
    if item in df:
        dup.add(item)
    df[item] = idx
line = sys.stdin.readline()
b = line.strip().split(" ")
flag = True
for item in b:
    if item not in df:
        print "Impossible"
        flag = False
        break
if flag:
    for item in b:
        if item in dup:
            print "Ambiguity"
            flag = False
            break
if flag:
    print "Possible"
    for item in b:
        print df[item],
    print
