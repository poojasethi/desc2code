#include<cstdio>
#include<queue>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int X[600],Y[600],Z[600];
int a[600],b[600],v[600];
int n,m;
int main()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		scanf("%d%d%d",&X[i],&Y[i],&Z[i]);
	scanf("%d",&m);
	for(int i=1;i<=m;i++)
		scanf("%d%d%d",&a[i],&b[i],&v[i]);
	int ans=0;
	for(int i=1;i<=n;i++)
	{
		int ret=0x7fffffff;
		int len=(X[i]+Y[i])*2;
		for(int j=1;j<=m;j++)
		{
			int bb=a[j]/Z[i];
			if(bb==0) continue;
			bb*=b[j];
			int nn=len/bb;
			if(nn*bb<len) nn++;
			ret=min(ret,nn*v[j]);
		}
		ans+=ret;
	}
	printf("%d\n",ans);
} 
