import sys,math
if __name__=='__main__':
    n=int(sys.stdin.readline())
    for abc in range(n):
        a=sys.stdin.readline()
        arr=[0]*52
        for i in a:
            if ord(i)>=97:
                arr[ord(i)-97+26]+=1
            elif ord(i)>=65:
                arr[ord(i)-65]+=1
        myfact=1
        tot=0
        for i in arr:
            tot+=i
            myfact*=math.factorial(i)
        totfact=math.factorial(tot)
        ans=totfact/myfact
        ans=ans%(10**9+7)
        print ans
