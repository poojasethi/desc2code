#include <bits/stdc++.h>

using namespace std;

#define ll long long

const int MaxN=2E3+10;
int x[MaxN],y[MaxN];

int32_t main(){
	int n;
	scanf("%d",&n);
	for (int i=0;i<n;++i)
		scanf("%d %d",&x[i],&y[i]);
	ll ans=1LL*n*(n-1)*(n-2)/6;
	for (int i=0;i<n;++i)
		for (int j=i+1;j<n;++j)
			for (int l=j+1;l<n;++l)
				if ((x[j]-x[i])*(y[l]-y[i])==(y[j]-y[i])*(x[l]-x[i]))
					--ans;
	printf("%I64d\n", ans);
}