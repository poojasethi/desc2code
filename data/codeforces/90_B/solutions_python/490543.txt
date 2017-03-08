from string import *

n, m = map(int, raw_input().split())
cj = [[0] * 26 for j in xrange(n)]
ci = [[0] * 26 for i in xrange(m)]

lines = []
for j in xrange(n):
    line = map(lowercase.index, raw_input().strip())
    lines.append(line)
    for i, a in enumerate(line):
        cj[j][a] += 1
        ci[i][a] += 1

print "".join([lowercase[a] if cj[j][a] == 1 and ci[i][a] == 1 else "" for j, line in enumerate(lines) for i, a in enumerate(line)])
