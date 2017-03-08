from collections import deque;
import sys

[n, m, s] = map(int, sys.stdin.readline().split());
c = list (map(int, sys.stdin.readline().split()));

a = [ [] for i in range (m + 1)];
for i in range (n):
	a[c[i]].append (i + 1);

ans = 1;
for i in range (1, m + 1):
	
	lc = len (a[i]);
	if lc == 0:
		continue
	q = deque([0]); cnt = 0; j = 0;
	while j + 1 < lc:
		j += 1;
		cnt += a[i][j] - a[i][j-1] - 1;
		q.append (j);

		while len (q) > 1 and cnt > s:
			cnt -= a[i][q[0]+1] - a[i][q[0]] - 1;
			q.popleft();
		ans = max (ans, len(q));
print (ans);
		
		
		
	

