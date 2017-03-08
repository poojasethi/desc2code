r,c=map(int,raw_input().split())
p=[]
for i in range(r):
    p.append([i for i in raw_input()])
X,Y=[],[]
for i in p:
    X.append(i.count('*'))

for i in range(c):
    ic=0
    for j in range(r):
        if p[j][i]=='*':
            ic+=1
    Y.append(ic)


ctr=sum(X)
            
if ctr==0:
    print "YES"
    print "1 1"
else:
    #print X,Y,ctr
    flag=False
    for i in range(r):
        for j in range(c):
            ret=X[i]+Y[j]-1 if p[i][j]=='*' else X[i]+Y[j]
            if ret==ctr :
                print "YES\n",i+1,j+1
                flag=True
                break
        if flag:
            break
    if not flag:
        print "NO"