import sys
s = sys.stdin.readline();
ls = len (s);
cntL = [0] * (ls + 1);
for i in range (1, ls + 1):
	cntL[i] = cntL[i-1];
	if s[i-1].islower():
		cntL[i] += 1;

ans = cntL[ls]; cnt = 0;
for i in range (ls - 1, -1, -1):
	if s[i].isupper():
		cnt += 1;
	ans = min (ans, cnt + cntL[i]);
print (ans);
	
	
	
