#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

#define maxn 100010
#define HP 1684593863

struct atype
{
	int ty,v; char ch;
};
atype op[maxn];

int depth2[maxn], lg2[maxn], depth1[maxn];
LL hash2[maxn][20], p[maxn][20];
LL ex[maxn];
char upedge[maxn];

int cmp(int x, int y)
{
	if (x==y) return 0;
	repd(k,19,0)
	{
		if ((1<<k)>depth2[x] || (1<<k)>depth2[y]) continue;
		if (hash2[x][k]==hash2[y][k]) x=p[x][k], y=p[y][k];
	}
	if (x==1 && y==1) return 0;
	if (x==1) return 1;
	if (y==1) return 0;
	return upedge[x]<upedge[y];
}

int movedep(int x, int y)
{
	while (y) x=p[x][lg2[y&-y]], y-=y&-y;
	return x;
}

int sa[maxn], where[maxn];
int l[maxn], r[maxn];

struct treearray
{
	int n; int ta[maxn];
	void clear(int _n)
	{
		n=_n; memset(ta,0,sizeof ta);
	}
	void serere(int x, int y)
	{
		while (x<=n) ta[x]+=y, x+=x&-x;
	}
	int query(int x)
	{
		int res=0;
		while (x) res+=ta[x], x-=x&-x;
		return res;
	}
	int query(int x, int y)
	{
		return query(y)-query(x-1);
	}
};

void lemon()
{
	ex[0]=1; rep(i,1,maxn-1) ex[i]=ex[i-1]*HP;
	lg2[1]=0; rep(i,2,maxn-1) lg2[i]=lg2[i>>1]+1;
	int qa; scanf("%d",&qa);
	int t1=1, t2=1; depth2[1]=0;
	rep(i,1,qa)
	{
		static char buf[100]; int x,y; scanf("%d%d%s",&x,&y,buf);
		op[i].ty=x; op[i].v=y; op[i].ch=buf[0];
		if (x==2)
		{
			t2++; depth2[t2]=depth2[y]+1; upedge[t2]=op[i].ch; 
			p[t2][0]=y; hash2[t2][0]=op[i].ch;
			rep(k,1,lg2[depth2[t2]]) 
			{
				p[t2][k]=p[p[t2][k-1]][k-1];
				hash2[t2][k]=hash2[p[t2][k-1]][k-1]*ex[1<<(k-1)]+hash2[t2][k-1];
			}
		}	
	}
	rep(i,1,t2) sa[i]=i;
	stable_sort(sa+1,sa+t2+1,cmp);
	rep(i,1,t2) where[sa[i]]=i;
	
	static treearray ta, tb;
	ta.clear(t2); ta.serere(where[1],1);
	tb.clear(t2); tb.serere(1,1);
	LL final=1; int t3=1;
	l[1]=1; r[1]=t2; depth1[1]=0;
	rep(cq,1,qa)
	{
		int ty=op[cq].ty, v=op[cq].v; char ch=op[cq].ch;
		if (ty==1)
		{
			t1++; depth1[t1]=depth1[v]+1;
			if (l[v]>r[v]) 
			{ 
				l[t1]=l[v]; 
				r[t1]=r[v];
			}
			else
			{
				{
					if (upedge[movedep(sa[l[v]],depth1[t1]-1)]>ch) 
						r[t1]=l[v]-1;
					else
					{
						int left=l[v], right=r[v];
						while (left!=right)
						{
							int mid=(left+right+1)/2;
							if (upedge[movedep(sa[mid],depth1[t1]-1)]<=ch) left=mid; else right=mid-1;
						}
						r[t1]=left;
					}
				}
				
				{
					if (upedge[movedep(sa[r[v]],depth1[t1]-1)]<ch)
						l[t1]=r[v]+1;
					else
					{
						int left=l[v], right=r[v];
						while (left!=right)
						{
							int mid=(left+right)/2;
							if (upedge[movedep(sa[mid],depth1[t1]-1)]>=ch) right=mid; else left=mid+1;
						}
						l[t1]=left;
					}
				}
			}		
			if (l[t1]<=r[t1]) 
			{
				final+=ta.query(l[t1],r[t1]);
				tb.serere(l[t1],1); tb.serere(r[t1]+1,-1);
			}
		}
		else
		{
			t3++; ta.serere(where[t3],1);
			final+=tb.query(where[t3]);
		}
		printf("%I64d\n",final);
	}
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("game.in","r",stdin);
	#endif
	lemon();
	return 0;
}