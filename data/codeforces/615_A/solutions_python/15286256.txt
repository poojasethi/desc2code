R=lambda:map(int,raw_input().split())
n,m=R()
a=[]
for i in range(n): a+=R()[1:]
print ["NO", "YES"][list(set(a))==range(1,m+1)]
