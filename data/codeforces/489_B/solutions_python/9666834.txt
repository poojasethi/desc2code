n = int(raw_input())
boys = [int(x) for x in raw_input().split()]

m = int(raw_input())
girls = [int(x) for x in raw_input().split()]

boys.sort()
girls.sort()

pairs = 0

for i in range(n-1,-1,-1):
	boy = boys[i]
	for j in range(m-1,-1,-1):
		if girls[j]==0:
			continue
		if abs(boy-girls[j])<=1:
			pairs+=1
			girls[j]=0
			break

print pairs
