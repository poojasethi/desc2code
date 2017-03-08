n = input()
d = dict()
for i in range(n):
    s = raw_input()
    d.setdefault(s, -1)
    d[s] += 1
    if d[s] == 0:
        print 'OK'
    else:
        print s + str(d[s])
