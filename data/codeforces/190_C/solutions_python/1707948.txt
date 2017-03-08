n = int(raw_input())
try:
    s=[]
    rs=[]
    ff=0
    for x in raw_input().split():
        #        print x,s,rs
        if ff==1 and len(s)==0:
            raise Exception("shit")
        ff=1
        if x=="pair":
            rs.append("pair<")
            s.append(">")
            s.append(",")
        else:
            rs.append("int")
            while len(s)>0:
                xx=s.pop()
                rs.append(xx)
                if xx==",":
                    break
    if len(s)!=0:
        raise Exception("shit2")
    print "".join(rs)    
except:
    print "Error occurred"

