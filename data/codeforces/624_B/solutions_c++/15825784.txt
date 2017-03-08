#include <bits/stdc++.h>

using namespace std;

#define int long long

int a[30];

int32_t main(){
	int n;
	cin >> n;
	for (int i=0;i<n;++i)
		cin >> a[i];
	sort(a,a+n);
	int ans=a[n-1];
	int k=a[n-1]-1;
	for (int i=n-2;i>=0;--i){
		ans+=min(a[i],k);
		k=min(a[i],k);
		k=max(k-1,0LL);
	}
	cout << ans;
}