#include <bits/stdc++.h>
#define maxn 1020000
using namespace std;
long long t[maxn];
int n,m;
long long ans;
const long long oo=1000003;

typedef long long LL;

LL inv(LL x)
{
	if (x==1) return 1;
	else return (oo-oo/x)*inv(oo%x)%oo;
}

LL com(LL x, LL y)
{
	return t[x]*inv(t[x-y]*t[y]%oo)%oo;
}

int main()
{
	t[0]=1;
	for (int i=1;i<=1000000;i++) t[i]=(t[i-1]*i)%oo;
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;i++)
		ans=(ans+com(i+m-1,m-1))%oo;
	printf("%d\n",ans);
	return 0;
}