n, m = map(int, raw_input().split())

lu = m
rd = 0

fst = None
lst = None

draw = []
for i in xrange(n):
    draw.append(list(raw_input()))

    for j in xrange(m):
        if draw[i][j] == "*":
            if fst == None:
                fst = i
                lst = i
            if lu > j:
                lu = j
            if rd < j:
                rd = j
            if i > lst:
                lst = i    
###print fst, lu, lst, rd

for i in xrange(fst, lst+1):
    print "".join(draw[i][lu:rd+1])
