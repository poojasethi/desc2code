#include <bits/stdc++.h>

using namespace std;

#define int long long

const int MaxN=5E5+10;
int p[MaxN];
int sum[MaxN],dp[MaxN];

int32_t main(){
	int n;
	cin >> n;
	for (int i=1;i<=n;++i){
		cin >> p[i];
		sum[i]=sum[i-1]+p[i];
	}
	string s="#",t;
	cin >> t;
	s+=t;
	for (int i=1;i<=n;++i){
		dp[i]=dp[i-1];
		if (s[i]=='B'){
			dp[i]+=p[i];
		}
	}
	int ans=dp[n];
	for (int i=1;i<=n;++i)
		ans=max(ans,dp[n]-dp[i]+sum[i]-dp[i]);
	for (int i=n;i>=1;--i)
		ans=max(ans,dp[i-1]+sum[n]-sum[i-1]-dp[n]+dp[i-1]);
	cout << ans;
}