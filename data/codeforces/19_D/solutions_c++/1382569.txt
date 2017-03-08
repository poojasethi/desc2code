#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
using namespace std;
const int M=220010;
int flag[M],xan[M<<2];
int max(int a,int b) {return a<b?b:a;}
struct Node
{
	int x,y;
	bool operator < (const Node &tp)const 
	{
		if(x!=tp.x) return x<tp.x;
		return y<tp.y;
	}
}a[M],x[M],ans,null;
void Up(int rt){xan[rt]=max(xan[rt<<1],xan[rt<<1|1]);}
bool cmpxy(Node a,Node b){if(a.x!=b.x) return a.x<b.x;return a.y<b.y;}
void Update(bool f,int X,int p,int l,int r,int rt)
{
	if(l==r) {if(f) xan[rt]=p;else xan[rt]=-1;return;}
	int mid=(l+r)>>1;
	if(X<=mid) Update(f,X,p,lson);
	else Update(f,X,p,rson);
	Up(rt);
}
void Query(Node p,int l,int r,int rt)
{
	if(x[r].x<=p.x||xan[rt]<=p.y) return;
	if(l==r) ans=x[l];
	int mid=(l+r)>>1;
	Query(p,lson);
	if(ans.x==-1) Query(p,rson);
}
int main()
{
	memset(xan,-1,sizeof(xan));
	int n,i,m=0;
	null.x=null.y=-1;
	char tr[10];
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%s%d%d",tr,&a[i].x,&a[i].y);
		if(tr[0]=='a') {x[m++]=a[i];flag[i]=1;}
		else if(tr[0]=='f') {x[m++]=a[i];flag[i]=2;}
		else flag[i]=0;
	}
	sort(x,x+m,cmpxy);
    for(i=0;i<n;i++)
	{
		int now=lower_bound(x,x+m,a[i])-x;
		if(flag[i]<2) Update(flag[i],now,a[i].y,0,m-1,1);
		else 
		{
			ans=null;
			Query(a[i],0,m-1,1);
			if(ans.x==-1) puts("-1");
			else printf("%d %d\n",ans.x,ans.y);
		}
	}
	return 0;
}