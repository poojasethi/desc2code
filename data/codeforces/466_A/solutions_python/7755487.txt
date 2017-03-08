n,m,a,b = [int(x) for x in raw_input().split()]

left = n%m
s1=(n/m)*b+left*a
s2=n*a
s3=(n/m+1)*b

print min(s1,min(s2,s3))
