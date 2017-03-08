l,r=map(int,raw_input().split())
res=0

while (l%10!=0)and(r>=l):
    if str(l)[0]==str(l)[-1]:
        res+=1
    	#print l
    l+=1
while (r%10!=9)and(r>=l):
    if str(r)[0]==str(r)[-1]:
        res+=1
        #print r
    r-=1
res+=(r-l+1)/10
print res    