# coding =utf-8
I = lambda:map(int,raw_input().split())
n = int(input())
a = sorted(I())
m = int(input())
b = sorted(I())
i,j,ans = 0,0,0
while i<n and j <m:
	if abs(a[i]-b[j])<=1:
		i+=1
		j+=1
		ans += 1
	else:
		if a[i]<b[j]:
			i += 1
		else:
			j += 1
print ans