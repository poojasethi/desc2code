t=raw_input()
t=int(t)
while t>0:
    f,m=raw_input().split()
    f=int(f);
    m=int(m);
    if m%f==0:
        print "CORRECT"
    else:
        print "WRONG"
    t=t-1