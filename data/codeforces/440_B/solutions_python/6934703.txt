n = int(input())
a = map(int, raw_input().split())
average = sum(a) / n;
answer = 0;
pre = 0
for i in xrange(n):
	if pre > 0:
		answer += pre;
		if pre > a[i]:
			pre -= a[i];
			a[i] = 0;
		else :
			a[i] -= pre
			pre = 0;
	if a[i] > average:
		answer += a[i] - average;
		a[i+1] += a[i] - average;
	else :
		pre += average - a[i];

print answer
