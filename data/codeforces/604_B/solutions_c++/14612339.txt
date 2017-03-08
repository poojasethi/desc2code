#include <bits/stdc++.h>

using namespace std;

const long long MaxN=1E5+10;
long long a[MaxN];

int main(){
	long long n,k;
	cin >> n >> k;
	for (long long i=0;i<n;++i)
		cin >> a[i];
	long long mx=a[n-1];
	for (long long i=0;i<2*(n-k);i+=2)
		mx=max(mx,a[i]+a[2*(n-k)-i-1]);
	cout << mx;
}