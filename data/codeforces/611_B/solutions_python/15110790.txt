a,b=map(int,raw_input().split())
ans=0
for i in xrange(2,64):
    for j in xrange(1,i):
        x = eval('0b'+'1'*j+'0'+'1'*(i-j-1))
        if a <= x <= b: ans += 1
print ans
