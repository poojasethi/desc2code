import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        s=sys.stdin.readline().strip()
        q=s[::-1]
        if s==q:
            print 'YES'
        else:
            print 'NO'
        
