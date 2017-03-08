# coding =utf-8
s = raw_input()
t = s[-1]
temp=-3
ans =""
for i in range(len(s)-2,-1,-1):
	if int(s[i])%2==0 and temp<0:
		temp=i
	elif int(s[i])%2==0 and int(s[i])<int(t):
		temp = i
if temp >=0:
	for i in range(len(s)):
		if i == temp:
			ans +=s[-1]
			continue
		if i == len(s)-1:
			ans +=s[temp]
			continue
		ans += s[i]
	print ans
else:
	print -1