R=lambda:map(int,raw_input().split())
n,m,k=R()
a=R().count(1)
print max(0,max(n-a-k,0)+a-m)