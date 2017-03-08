#include <bits/stdc++.h>
using namespace std;

#define F(i,n) for(long long i=0;i<n;i++)
#define FE(i,n) for(int i=0;i<=n;i++)
#define FR(i,n) for(int i=n;i>0;i--)
#define FRE(i,n) for(int i=n;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define pii pair <long long , long long>
#define LL long long
#define gc getchar_unlocked
#define pc putchar_unlocked

inline void get(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

inline void getll(LL &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

vector < pii > watch;
pii adj[1005][1005];
priority_queue < pii , vector < pii > , greater < pii > > pq;
bool visited[1005];

LL dijkstra(int n)
{
	F(i,n)
	{
		pii tmp = pq.top();
		visited[tmp.second] = true;

		if (tmp.second == watch.size()-1)
			return tmp.first;

		for (int j=0; j<n; j++)
		{
			if (visited [j])
				continue;
			else
				pq.push(mp(tmp.first + adj[tmp.second][j].first, j));
		}

		while (pq.size()>0 && visited[(pq.top()).second])
			pq.pop();
	}

	return 0;
}

int main()
{
	LL n;
	getll(n);

	LL x,y;

	watch.push_back(mp(0,0));

	F(i,n+1)
	{
		getll(x);
		getll(y);

		watch.push_back(mp(x,y));
	}

	LL sz = watch.size();

	F(i,sz)
		F(j,sz)
			adj[i][j] = mp((pow((watch[j].first - watch[i].first),2) + pow((watch[j].second - watch[i].second),2)) , j);			

	pq.push(adj[0][0]);

	printf("%lld\n",dijkstra(sz));

	return 0;
}