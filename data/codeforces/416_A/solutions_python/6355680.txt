n = int(raw_input())
minV = -2*pow(10, 9)
maxV = 2*pow(10, 9)

for i in xrange(n):
    eq, num, yn = raw_input().split()
    isEq = True if len(eq) == 2 else False
    num = int(num)

    if yn == 'N':
        eq = '<' if eq[0] == '>' else '>'
        isEq = not isEq

    if eq[0] == '>':
        if not isEq:
            num+=1
        if minV < num:
            minV = num
    else:
        if not isEq:
            num-=1
        if maxV > num:
            maxV = num

if minV > maxV:
    print 'Impossible'
else:
    print minV