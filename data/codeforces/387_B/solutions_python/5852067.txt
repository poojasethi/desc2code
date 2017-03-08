#author: uniqueinx
#codeforces: George and Round
n,m = raw_input().rsplit(' ')
a = raw_input().rsplit(' ')
b = raw_input().rsplit(' ')
i = j = 0
while i < int(n) and j < int(m):
	if int(b[j]) >= int(a[i]):
		i+=1
	j+=1
print int(n) - i


