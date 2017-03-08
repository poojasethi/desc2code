dic={}
n, q = map(int, raw_input().split())
li = map(int, raw_input().split())
for i in xrange(q):
    l, r = map(int, raw_input().split())
    tli=li[l:r+1]
    s=str(l) + '+' + str(r)
    if s not in dic:
        dic[s] = max(tli) - min(tli)
    print dic[s]