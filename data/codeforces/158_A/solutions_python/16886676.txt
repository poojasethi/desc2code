l=lambda:map(int,raw_input().split());n,k=l();a=l()
print sum(v>=max(1,a[k-1])for v in a)