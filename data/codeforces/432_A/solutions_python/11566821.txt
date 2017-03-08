def f(x):
	global k
	return x+k <= 5
n,k = map(int,raw_input().split())
data = map(int,raw_input().split())
print len(filter(f,data))/3