#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <map>
#include <vector>
#include <utility>
#include <set>

#define MOD (1000000007)
#define MAXINT 1e9

using namespace std;
typedef long long int ll;

struct xx
{
	int r[12];
}a[800005];

struct node
{
	int lazy;
	struct xx list;
}tree[1<<22];

void initialise(int node,int l,int r)
{
	if(l==r)	
	{
		tree[node].lazy=0;
		tree[node].list=a[l];
		return;
	}
	initialise(node<<1,l,(l+r)>>1);
	initialise((node<<1)+1,((l+r)>>1)+1,r);
	for(int i=0;i<12;i++)
		tree[node].list.r[i]=max(tree[node<<1].list.r[i],tree[(node<<1)+1].list.r[i]);
}

void update(int node,int node_l,int node_r,int q_l,int q_r,int f)
{
	if(tree[node].lazy)
	{
		int f=tree[node].lazy;
		int xx[12];
		for(int i=0;i<12;i++)	xx[i]=tree[node].list.r[i];
		for(int i=0;i<12;i++)
			tree[node].list.r[i]=xx[(i+f)%12];
		if(node_l!=node_r){
		tree[node<<1].lazy=(tree[node<<1].lazy+f)%12;
		tree[(node<<1)+1].lazy=(tree[(node<<1)+1].lazy+f)%12;}
		tree[node].lazy=0;
	}
	if(node_l>q_r || node_r<q_l)	return;
	else if(node_l>=q_l && node_r<=q_r)
	{
		int xx[12];
		for(int i=0;i<12;i++)	xx[i]=tree[node].list.r[i];
		for(int i=0;i<12;i++)
			tree[node].list.r[i]=xx[(i+f)%12];
		if(node_l!=node_r)
		{
			tree[node<<1].lazy=(tree[node<<1].lazy+f)%12;
			tree[(node<<1)+1].lazy=(tree[(node<<1)+1].lazy+f)%12;
		}
		return;
	}
	update(node<<1,node_l,(node_r+node_l)>>1,q_l,q_r,f);
	update((node<<1)+1,((node_l+node_r)>>1)+1,node_r,q_l,q_r,f);
	for(int i=0;i<12;i++)
		tree[node].list.r[i]=max(tree[node<<1].list.r[i],tree[(node<<1)+1].list.r[i]);
}

int query(int node,int node_l,int node_r,int q_l,int q_r)
{
	if(tree[node].lazy)
	{
		int f=tree[node].lazy;
		int xx[12];
		for(int i=0;i<12;i++)	xx[i]=tree[node].list.r[i];
		for(int i=0;i<12;i++)
			tree[node].list.r[i]=xx[(i+f)%12];
		if(node_l!=node_r){
		tree[node<<1].lazy=(f+tree[node<<1].lazy)%12;
		tree[(node<<1)+1].lazy=(tree[(node<<1)+1].lazy+f)%12;}
		tree[node].lazy=0;
	}
	if(node_l>q_r || node_r<q_l)	return -1;
	else if(node_l>=q_l && node_r<=q_r)
	{
		return tree[node].list.r[0];
	}
	int x=query(node<<1,node_l,(node_r+node_l)>>1,q_l,q_r);
	int y=query((node<<1)+1,((node_l+node_r)>>1)+1,node_r,q_l,q_r);
	for(int i=0;i<12;i++)
		tree[node].list.r[i]=max(tree[node<<1].list.r[i],tree[(node<<1)+1].list.r[i]);
	return max(x,y);
}

int main()
{
	char x[6];
	int t,i,j,n,l,r,f,m;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf(" %s",x);
		a[i].r[0]=atoi(x);
		l=strlen(x);
		for(j=1;j<l;j++)
		{
			int e=0;
			for(int k=j;k<l;k++)	e=e*10+x[k]-'0';
			int f=0;
			for(int k=0;k<j;k++,e*=10)	f=f*10+x[k]-'0';
			a[i].r[j]=e+f;
		}
		int k=0;
		for(;j<12;j++,k++)	a[i].r[j]=a[i].r[k];
	}
	initialise(1,0,n-1);
	scanf("%d",&m);
	while(m--)
	{
		scanf("%d",&t);
		if(t==0)
		{
			scanf("%d%d%d",&l,&r,&f);
			update(1,0,n-1,l,r,f);
		}
		else
		{
			scanf("%d%d",&l,&r);
			printf("%d\n",query(1,0,n-1,l,r));
		}
	}
	return 0;
}