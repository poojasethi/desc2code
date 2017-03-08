n=input()
a=map(int, raw_input().split())
b=[0]*5
for x in a:
    b[x]+=1
res=b[3]+b[4]
b[1]=max(b[1]-b[3],0)
res+=(b[2]*2+b[1]+3)/4
print res