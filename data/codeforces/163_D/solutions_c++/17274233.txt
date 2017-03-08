#include<cstdio>
#include<cmath>
typedef long long ll;
int T,i,j,n,q[20];
ll A,B,C,a,b,c,M,MA,ans,v,p[20];
void cal(int s,ll now)
{
	if(now>M)return;
	if(s>n)
	{
		if(now<a)return;
		b=now,c=v/a/b;
		if(a*b+a*c+b*c<ans)
			ans=a*b+a*c+b*c,A=a,B=b,C=c;
		return;
	}
	if(q[s])
		q[s]--,cal(s,now*p[s]),q[s]++;
	cal(s+1,now);
}
void dfs(int s,ll now)
{
	if(now>MA)return;
	if(s>n)
	{
		if(a=now,v/a+2*a*sqrt(v/a)<ans)
		M=sqrt(v/a)+1e-8,cal(1,1);return;
	}
	if(q[s])
		q[s]--,dfs(s,now*p[s]),q[s]++;
	dfs(s+1,now);
}
int main()
{
	for(scanf("%d",&T);T--;)
	{
		scanf("%d",&n);
		for(v=i=1;i<=n;i++)
		{
			scanf("%I64d%d",&p[i],&q[i]);
			for(j=1;j<=q[i];j++)v*=p[i];
		}
		ans=5e18,A=0,MA=pow(v,1./3)+1e-8,dfs(1,1);
		printf("%I64d %I64d %I64d %I64d\n",2*ans,A,B,C);
	}
}