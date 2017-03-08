import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    area=[]
    for abc in range(n):
        a,b,c,d=sys.stdin.readline().split()
        x1.append(int(a))
        x2.append(int(c))
        y1.append(int(b))
        y2.append(int(d))
        area.append((int(d)-int(b))*(int(c)-int(a)))
    areagot=(min(x1)-max(x2))*(min(y1)-max(y2))
    if min(x1)-max(x2)==min(y1)-max(y2):
        if areagot==sum(area):
            print "YES"
        else:
            print "NO"
    else:
        print 'NO'
            
