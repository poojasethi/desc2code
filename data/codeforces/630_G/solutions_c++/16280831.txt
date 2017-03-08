#include <bits/stdc++.h>

using namespace std;

#define int long long

int32_t main(){
	int n;
	cin >> n;
	int ans=n*(n+1)*(n+2)*(n+3)*(n+4)/120;
	ans*=n*(n+1)*(n+2)/6;
	cout << ans;
}