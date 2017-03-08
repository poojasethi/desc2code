import sys
n = int (sys.stdin.readline ());
p = list (map (int, sys.stdin.readline ().split ()));
c = list (map (int, sys.stdin.readline ().split ()));
cnt = [0 for i in range (5)];
res = 0
for i in range (n):
	res += p[i];
	for i in range (4, -1, -1):
		if res >= c[i]:
			cnt[i] += res // c[i];
			res %= c[i];
print (' '.join ([str(x) for x in cnt]));
print (res)
