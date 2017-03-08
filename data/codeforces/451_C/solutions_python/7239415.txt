num = raw_input()
num=int(num)
while num>0:
    s=raw_input()
    inp=map(int,s.split())
    sign = (-1,1)
    done = False
    if inp[0]%3!=0:
        print "no"
    else:  
        for i in sign:
            for j in sign:
                d1=i*inp[2]
                d2=j*inp[3]
                k=inp[1]
                n=inp[0]
                x2=(k+d2-d1)/3
                if (k+d2-d1)%3!=0:
                    continue
                if x2>=0 and x2<=k:
                    x1=x2+d1
                    x3=x2-d2
                    if x1>=0 and x1<=k and x3>=0 and x3<=k:
                        if x1<=n/3 and x2<=n/3 and x3<=n/3:
                            done=True
                            break
            if done==True:
                break
        if done:
            print "yes"
        else:
            print "no"
    num=num-1    
