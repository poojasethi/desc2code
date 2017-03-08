for _ in xrange(int(input())):
    n=int(input())
    dic={}
    for i in xrange(n):
        s=raw_input()
        if s not in dic:
            dic[s]=1
        else:
            dic[s]+=1
    count=0
    for i in dic:
        if(dic[i]%2!=0):
            count+=1
    print count