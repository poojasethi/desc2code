#include <cstdio>
#include <algorithm>
using namespace std;
 
typedef long long LL;
 
const int N = 200000;
int row[N+1];
int diag_mask[N];
int lose[N+1];
 
struct query
{
	int x,y,id,sign;
	query(){}
	query(int x_,int y_,int id_,int sign_){x=x_;y=y_;id=id_;sign=sign_;}
	bool operator<(const query &q) const
	{
		return x<q.x;
	}
};
 
const int maxT = 100000;
query a[4*maxT];
int f[N+1];
int ans_num[maxT];
LL ans_denom[maxT];
 
LL gcd(LL a,LL b)
{
	LL c;
	while(b) c=a%b,a=b,b=c;
	return a;
}
 
void add(int x,int d)
{
	for(;x<=N;x+=x&-x) f[x]+=d;
}
 
int getsum(int x)
{
	int s=0;
	for(;x>0;x-=x&-x) s+=f[x];
	return s;
}
 
int main()
{
	int d;
	scanf("%d",&d);
	int x,y,y0=1;
	int dg=0;
	for(x=1;x<=N;x++) if(!row[x])
	{
		for(;y0<=N && row[y0];y0++);
		if(y0>N) break;
		for(;dg<N && diag_mask[dg]==(1<<d)-1;dg++);
		for(y=max(y0,x+dg);y<=N && ((diag_mask[y-x] & 1<<(x%d)) || row[y]);y++);
		if(y<=N)
		{
			lose[x]=y;
			lose[y]=x;
			row[y]=1;
			diag_mask[y-x] |= 1<<(x%d);
		}
		row[x]=1;
	}
 
	int T;
	scanf("%d",&T);
	int i;
	int len=0;
	for(i=0;i<T;i++)
	{
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		x1--;y1--;
		ans_num[i]=0;
		ans_denom[i]=LL(x2-x1)*(y2-y1);
		a[len++]=query(x1,y1,i,1);
		a[len++]=query(x1,y2,i,-1);
		a[len++]=query(x2,y1,i,-1);
		a[len++]=query(x2,y2,i,1);
	}
	sort(a,a+len);
	i=0;
	for(x=1;x<=N;x++)
	{
		if(lose[x]) add(lose[x],1);
		for(;i<len && a[i].x<x;i++);
		for(;i<len && a[i].x==x;i++)
			ans_num[a[i].id] += a[i].sign * getsum(a[i].y);
	}
	for(i=0;i<T;i++)
	{
		LL p=ans_num[i];
		LL q=ans_denom[i];
		LL g=gcd(p,q);
		p/=g;
		q/=g;
		printf("%lld/%lld\n",p,q);
	}
	return 0;
}