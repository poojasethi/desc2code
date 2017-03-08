n, a, b = map(int, raw_input().split());
s = raw_input();
if len(s)/n < a or len(s)/n > b:
    print "No solution"
elif len(s)%n and len(s)/n + 1 > b:
    print "No solution"
else:
    j = 0
    for i in range(n):
        x = str()
        for k in range(len(s)/n + (i<len(s)%n)):
            x += s[j]
            j += 1
        print x


