n,k=map(int,raw_input().split())
a=map(lambda i:5-int(i),raw_input().split())
print len(filter(lambda x:x>=k,a))/3