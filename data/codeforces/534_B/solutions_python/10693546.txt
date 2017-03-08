# coding =utf-8
I=lambda:map(int,raw_input().split())
v1,v2 = I()
t,d = I()
now = []
j = v1
for i in range(t):
	now.append(j)
	j += d
j = v2
i = t-1
while True:
	now[i]=j
	if now[i-1]-j<=d:
		break
	j+=d
	i -= 1
print sum(now)