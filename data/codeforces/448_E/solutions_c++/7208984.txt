#include <bits/stdc++.h>
using namespace std;
#define ll __int64
ll a[100000],t,cnt;
void DFS(ll n,ll k)
{
	if (cnt>=1e5)
		return;
	if (k==0 || n==1)
	{
		cnt++;
		printf("%I64d ",n);
		return;
	}
	for (ll i=0;i<t && n>=a[i];i++)
		if (n % a[i]==0)
			DFS(a[i],k-1);
	return;
}
int main()
{
	t=0;
	ll n,k;
	scanf("%I64d%I64d",&n,&k);
	for (ll i=1;i*i<=n;i++)
		if (n % i==0)
		{
			a[t++]=i;
			if (i!=n/i)
			a[t++]=n/i;
		}
	cnt=0;
	sort(a,a+t);
	DFS(n,k);
	return 0;
}
