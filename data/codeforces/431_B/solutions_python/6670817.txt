import itertools;
g = [];
for i in xrange(5):
  a = map(int, raw_input().split());
  g.append(a);
p = list(itertools.permutations([0,1,2,3,4],5));
ans = 0;
for i in xrange(len(p)):
  	b = p[i];
	tmp = 0;
	tmp += g[b[0]][b[1]] + g[b[1]][b[0]];
	tmp += g[b[2]][b[3]] + g[b[3]][b[2]];
	tmp += g[b[1]][b[2]] + g[b[2]][b[1]];
	tmp += g[b[3]][b[4]] + g[b[4]][b[3]];
	tmp += g[b[2]][b[3]] + g[b[3]][b[2]];
	tmp += g[b[3]][b[4]] + g[b[4]][b[3]];
	ans = max(ans, tmp);
print ans;


