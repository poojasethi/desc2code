I=lambda:map(int,raw_input().split())
n,d=I()
s=sum(I())
res=(d-s)/5
if d-s<(n-1)*10:
    print -1
else:
    print res
