/**
 *       Compiler:  gcc
 *         Author:  bdep__  
 *        Created:  03/24/2012 09:50:59 PM
 ***/

#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <cmath>
#include <iostream>
#include <algorithm>
#define N 100010
#define M 1000010
#define S 1000100
#define MOD 1000000007

typedef long long LL;
using namespace std;

inline int L(int i){ return i<<1; }
inline int R(int i){ return (i<<1)|1; }
inline int B(int i){ return 1<<i; }
inline int low_bit(int x){ return x&(-x); }

struct shoe{ int s,c,i; }cus,pro[N];

int cmp_s(shoe a,shoe b){ return a.s<b.s; }
int cmp_c(shoe a,shoe b){ return a.c>b.c; }

int top,match[N];
bool v[N];
vector<int> E[N];

bool dfs(int now)
{
	int t;
	for(int i=0; i<E[now].size(); i++)
	{
		t=E[now][i];
		if(!v[t])
		{
			v[t]=1;
			if(match[t]==-1||(dfs(match[t])))
			{
				match[t]=now;
				return 1;
			}
		}
	}
	return 0;
}

int main()
{
	int x,y,z,n,m,cnt;
	LL ret;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		scanf("%d%d",&pro[i].c,&pro[i].s);
		pro[i].i=i+1;
	}
	sort(pro,pro+n,cmp_s);
	scanf("%d",&m);
	for(int i=0; i<m; i++)
	{
		scanf("%d%d",&x,&y);
		cus.c=x,cus.s=y;
		cus.i=i+1;
		z=lower_bound(pro,pro+n,cus,cmp_s)-pro;
		for(; pro[z].s==y||pro[z].s==y+1; z++)
			if(pro[z].c<=cus.c)
				E[pro[z].i-1].push_back(i);
	}
	sort(pro,pro+n,cmp_c);
	memset(match,-1,sizeof(match));
	ret=0,cnt=0;
	for(int i=0; i<n; i++)
	{
		memset(v,0,sizeof(v));
		if(dfs(pro[i].i-1))
			ret+=pro[i].c,cnt++;
	}
	printf("%I64d\n%d\n",ret,cnt);
	for(int i=0; i<m; i++)
		if(match[i]>-1)
			printf("%d %d\n",i+1,match[i]+1);
	return 0;
}
