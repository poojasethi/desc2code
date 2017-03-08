def check(name0,name1,alpha):
    for i in xrange(min(len(name0),len(name1))):
        if alpha.index(name0[i]) < alpha.index(name1[i]): return -1
        if alpha.index(name0[i]) > alpha.index(name1[i]): return i
    return -1 if len(name0) <= len(name1) else -2

alpha = list("abcdefghijklmnopqrstuvwxyz")
N = int(raw_input())
name = [raw_input() for i in xrange(N)]

for loop in xrange(2):
    for i in xrange(N):
        for j in xrange(i+1,N):
            p = check(name[i],name[j],alpha)
            if p > -1:
                a,b = alpha.index(name[i][p]),alpha.index(name[j][p])
                char = alpha.pop(b)
                alpha.insert(a,char)
            elif p == -2:
                print "Impossible"
                exit()
ans = True
for i in xrange(N):
    for j in xrange(i+1,N):
        if check(name[i],name[j],alpha) > -1:
            ans = False
            break
    if not ans: break
print "".join(alpha) if ans else "Impossible"
