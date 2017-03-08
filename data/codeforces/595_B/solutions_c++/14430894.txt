#include <bits/stdc++.h>

using namespace std;

long long n,k,a[100005],b[100005],x,nr,r,rez,i,c,t,m,sup,inf;

#define mod  1000000007

int main()
{
    cin>>n>>k;
    for (i=1;i<=n/k;++i)
        cin>>a[i];
    for (i=1;i<=n/k;++i)
        cin>>b[i];

    m=1;
    for (i=1;i<=k;++i)
        m*=10;
    --m;

    rez=1;
    for (i=1;i<=n/k;++i) {
        sup=m/a[i]+1;
		inf=m/10/a[i];

		r=(a[i]-(b[i]*(m/10+1))%a[i])%a[i];
		if (r+inf*a[i]>m/10) --inf;
		++inf;
		rez=((rez%mod)*(sup-inf)%mod)%mod;
	}

    cout<<rez%mod;
    return 0;
}
