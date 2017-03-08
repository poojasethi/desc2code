t=int(input())
for i in range(t):
    m,s=raw_input().split()
    m=int(m)
    s=s.replace("**","#")
    ar=s.split("*")
    ans=1
    for i in ar:
        if '#' in i:
            z=i.split("#")
            #print i,z
            ans1=pow(int(z[0]),int(z[1]),m)
            ans = (ans*ans1)%m
        else:
            ans=(ans*int(i))%m
    print ans
