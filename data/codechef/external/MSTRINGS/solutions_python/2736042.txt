import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        s=sys.stdin.readline().strip()
        flag=True
        for i in range(len(s)):
            j=len(s)-1
            while j>=0:
                p=s[i:j+1][::-1]
                #print p
                if p not in s:
                    flag=False
                    break
                j-=1
            if not flag:
                break
        if flag:
            print 'YES'
        else:
            print 'NO'
            
