import sys
def getMax(a):
    x=max(a)
    for i in range(len(a)):
        if a[i]==x:
            return i
    return -1
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        n,m,k=sys.stdin.readline().split()
        n=int(n)
        m=int(m)
        k=int(k)
        b=[]
        for j in range(n):
            a=sys.stdin.readline().strip()
            x=a.count('.')
            b.append(x)
        #print b
        for j in range(k):
            q=getMax(b)
            b[q]=m-b[q]
        print n*m-sum(b)
        
        
