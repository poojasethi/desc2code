a,b=map(int,raw_input().split())
i=0
while a>0 and b>0:
    if a==1 and b==1:
	    break
    if a<b:
        a+=1
        b-=2
    else:
        b+=1
        a-=2
    i+=1
    
print i    
