#include <bits/stdc++.h> 

using namespace std;

const int MaxN=1E5+10;
int dp[MaxN];

int main(){
	int n;
	cin >> n;
	for (int i=0;i<n;++i){
		int x;
		cin >> x;
		dp[x]=dp[x-1]+1;
	}
	cout << n-*max_element(dp,dp+n+1);
}