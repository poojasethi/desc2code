# your code goes here
v1, v2 = map(int, raw_input().split())
t, d = map(int, raw_input().split())
i = 1
sum1 = v1
while i<= t-2:
	sum1 = sum1 + min(v1 + i*d,v2 + (t-1)*d - i*d)
	i = i + 1
print sum1 + v2
