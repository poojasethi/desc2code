//Program question at: http://www.codechef.com/CRNM2012/problems/CRNM1205
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int maxio=1000000;
char buf[1000000], *s = buf + maxio;
inline char getc_(void) { if(s >= buf + maxio) { fread(buf,sizeof(char),maxio,stdin); s = buf; } return *(s++); }
inline int input() { char t = getc_(); int n=1,res=0; while(t!='-' && !isdigit(t)) t=getc_(); if(t=='-') { n=-1; t=getc_(); } while(isdigit(t)) { res  = 10*res + (t&15); t=getc_(); } return res*n; }

char **grid;
int **dist;
int sx,sy,ex,ey, m,n, num,k;
vector<int> path;

inline bool check(int x, int y)
{
	if(x < 0 || y < 0 || x >= m || y >= n) return 0;
	if(grid[x][y] == '#' || dist[x][y] != -1) return 0;
	return 1;
}

int solve()
{
	vector<int>::iterator i = path.begin();
	for(int a=0; a<k; a++,i++)
	{
		int x = (*i)/n, y = (*i)%n, nc = dist[x][y]+1;
		for(int a=x-1;check(a,y);a--)
			{ dist[a][y] = nc; path.push_back(a*n+y); if(a == ex && y == ey) return nc; num++; }
		for(int a=x+1;check(a,y);a++)
			{ dist[a][y] = nc; path.push_back(a*n+y); if(a == ex && y == ey) return nc; num++; }
		for(int a=y+1;check(x,a);a++)
			{ dist[x][a] = nc; path.push_back(x*n+a); if(x == ex && a == ey) return nc; num++; }
		for(int a=y-1;check(x,a);a--)
			{ dist[x][a] = nc; path.push_back(x*n+a); if(x == ex && a == ey) return nc; num++; }
	}
	return 0;
}

int f()
{
	k=1;
	path.push_back(sx*n+sy);
	dist[sx][sy] = 0;
	while(1)
	{
		num=0;
		int r = solve();
		if(r) return r;
		if(num == 0) return 0;
		path.erase(path.begin(), path.begin() + k);
		k = num;
	}
	return -1; // unreachable
}

int main()
{
	int t = input();
	while(t--)
	{
		m = input(); n = input();
		grid = new char*[m];
		dist = new int*[m];
		sx = input(); sy = input(); ex = input(); ey = input();
		for(int a=0;a<m;a++) { grid[a] = new char[n]; dist[a] = new int[n];
		for(int b=0;b<n;b++)
			{ char ch=' '; while( !(ch=='.' || ch=='#')) ch = getc_(); grid[a][b] = ch; dist[a][b] = -1; } }

		printf("%d\n",f());
		path.clear();
	}
	return 0;
}
