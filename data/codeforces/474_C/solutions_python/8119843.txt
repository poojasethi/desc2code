n = int(raw_input())

# def S(A):c=sum(A)/4.0;return set(A)==set((A[0]-c)*1j**i+c for i in range(4))
# S=lambda A:len(set(A))-1==len(set([abs(K-J)for K in A for J in A]))
# def S(A):c=sum(A)/4;d=A[0]-c;return{d+c,c-d,d*1j+c,c-d*1j}==set(A)
def S(p):return len(set(p))-1==len(set([pow(pow(a-c,2)+pow(b-d,2),.5)for a,b in p for c,d in p]))
while n:
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    c = map(int, raw_input().split())
    d = map(int, raw_input().split())
    al = [(a[0],a[1]),(a[2]-a[1]+a[3],a[3]-a[2]+a[0]),(2*a[2]-a[0],2*a[3]-a[1]),(a[2]+a[1]-a[3],a[2]+a[3]-a[0])]
    bl = [(b[0],b[1]),(b[2]-b[1]+b[3],b[3]-b[2]+b[0]),(2*b[2]-b[0],2*b[3]-b[1]),(b[2]+b[1]-b[3],b[2]+b[3]-b[0])]
    cl = [(c[0],c[1]),(c[2]-c[1]+c[3],c[3]-c[2]+c[0]),(2*c[2]-c[0],2*c[3]-c[1]),(c[2]+c[1]-c[3],c[2]+c[3]-c[0])]
    dl = [(d[0],d[1]),(d[2]-d[1]+d[3],d[3]-d[2]+d[0]),(2*d[2]-d[0],2*d[3]-d[1]),(d[2]+d[1]-d[3],d[2]+d[3]-d[0])]
    step = 1000000000
    for i1 in xrange(4):
        for i2 in xrange(4):
            for i3 in xrange(4):
                for i4 in xrange(4):
                    temp = [al[i1],bl[i2],cl[i3],dl[i4]]
                    if S(temp) and (al[i1][0]!=bl[i2][0]or al[i1][1]!=bl[i2][1] ):
                        if i1+i2+i3+i4<step:
                            step=(i1+i2+i3+i4)

    if step < 1000000000:
        print step
    else:
        print -1

    n -=1
