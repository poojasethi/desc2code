#include <bits/stdc++.h>
using namespace std;
#define g(n) scanf("%d",&n)
#define f(i,n) for(int i=0; i<n; i++)
#define mp make_pair
 
typedef pair<int,int> pii;
int ar[100000];
pii p[100000];
pii pn[100000];
int make_disjoint(int n)
{
	if(n==0)
		return 0;
	pn[0] = p[0];
	int l=1;
	for(int i=1; i<n; i++)
	{
		if(p[i].first <= pn[l-1].second)
			pn[l-1].second = max(p[i].second, pn[l-1].second);
		else
			pn[l++] = p[i];
	}
	return l;
}
 
int main()
{
	int t,n,m,a,b;
	g(t);
	while(t--)
	{
		g(n),g(m);
		f(i,n) g(ar[i]), ar[i]--; //make the numbers 0 based
		f(i,m)
		{
			g(a), g(b);
			a--,b--; //making indices 0 based
			p[i] = mp(a,b);
		}
		sort(p, p+m);
		m = make_disjoint(m);
		// now array is pn, and m is the size of pn
		f(i,m)
		{
			sort(ar+pn[i].first, ar+pn[i].second+1);
		}
 		bool flag = true;
 		f(i,n)
 		{
 			if(ar[i]!=i)
 			{
 				flag = false;
 				break;
 			}
 		}
		if(flag)
			printf("Possible\n");
		else
			printf("Impossible\n");
	}
} 