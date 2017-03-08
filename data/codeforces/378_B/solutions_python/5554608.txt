import sys
n=int(sys.stdin.readline())
A=[]
B=[]
T=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    T.append((a,i,0))
    T.append((b,i,1))
T.sort()
a=[0]*n
b=[0]*n
for i in range(n//2):
    a[i]=1
    b[i]=1
for i in range(n):
    if(T[i][-1]==0):
        a[T[i][1]]=1
    else:
        b[T[i][1]]=1
Ans=""
for i in range(n):
    Ans+=str(a[i])
Ans+="\n"
for i in range(n):
    Ans+=str(b[i])
sys.stdout.write(Ans)