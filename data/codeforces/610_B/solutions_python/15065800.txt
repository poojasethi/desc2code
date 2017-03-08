n=input()
a=map(int,raw_input().split())
l=min(a)
b=[i for i in xrange(n) if a[i]==l]
m=0
for i in xrange(len(b)):
    m=max(m,(b[i]-b[i-1])%n)
if m==0: m=n
print l*n+m-1
