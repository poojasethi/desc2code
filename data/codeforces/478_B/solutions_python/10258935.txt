n,m = map(int,raw_input().split())
a = n/m
b = n/m + 1
c = n-m + 1
print a*(a-1)/2*(m-n%m) + b*(b-1)/2*(n%m), c*(c-1)/2
