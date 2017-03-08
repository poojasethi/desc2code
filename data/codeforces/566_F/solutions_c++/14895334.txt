#include <bits/stdc++.h>

using namespace std;

const int MaxN=1E6+10;
int a[MaxN],dp[MaxN];

bool cmp(int a,int b){
	return a>b;
}

int main(){
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i=0;i<n;++i)
		cin >> a[i];
	sort(a,a+n,cmp);
	int ans=0;
	for (int i=0;i<n;++i){
		dp[a[i]]=1;
		for (int j=2*a[i];j<=MaxN;j+=a[i])
			dp[a[i]]=max(dp[a[i]],dp[j]+1);
		ans=max(ans,dp[a[i]]);
	}
	cout << ans;
}