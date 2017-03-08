a=[input() for _ in xrange(4)]
d=input()
c=0
for x in xrange(1,d+1):
    if any(x%i==0 for i in a):
        c+=1
print c