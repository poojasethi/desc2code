# coding =uft-8
s = map(int,raw_input().split())
s0 = map(int, raw_input().split())
s0.sort()
i = s[0]
ans = 0
while i-1>=0:
	ans += (s0[i-1]-1)*2
	i -= s[1]
print ans