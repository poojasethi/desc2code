l = [0] * 102
a = int(raw_input())
n = map(int, raw_input().split())
b = int(raw_input())
m = map(int, raw_input().split())
pairs = 0
for i in n:
	l[i] += 1

m.sort()
for i in m:
	if(l[i-1] > 0):
		l[i-1] -= 1
		pairs += 1
	elif(l[i] > 0):
		l[i] -= 1
		pairs += 1
	elif(l[i+1] > 0):
		l[i+1] -= 1
		pairs += 1
print pairs 