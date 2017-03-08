n,m=raw_input().split()
d={}
flag=False
for i in range(int(m)):
    u,v=raw_input().split()
    '''if u==v:
        flag=True
        break'''
    if u in d and v in d:
        flag=True
        break
    d[u]=d[v]=1
if flag:
    print "NO"
else:
    print "YES"
    
