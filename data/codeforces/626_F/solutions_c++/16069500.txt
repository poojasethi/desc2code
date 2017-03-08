#include <bits/stdc++.h>

#define MOD (int)1000000007

using namespace std;

int dp[202][202][1007];

int n, K;
int ar[207];

long long f(int idx, int og, int imb) {
	if (og < 0)
		return 0;
	if (imb > K)
		return 0;
	if (idx > n ) {
		return (og==0);
	}
	if (dp[idx][og][imb] != -1)
		return dp[idx][og][imb];

	long long ans = 0;
	int ximb =imb  +  og * (ar[idx] - ar[idx - 1]);
	ans = (ans + f(idx + 1, og, ximb ) *(og + 1) )%MOD; //isolated group
	ans = (ans + f(idx+1, og + 1, ximb )) % MOD; // open 1 new group
	ans = (ans + f(idx + 1, og - 1, ximb) * og)%MOD; //close 1 group
	dp[idx][og][imb] = ans;
	return ans;
}
int main() {
	cin >> n >> K ;
	for (int i = 1; i <= n; i++) cin >> ar[i];
	memset (dp, -1, sizeof(dp));
	sort(ar+1, ar + n+ 1);
	cout <<f(1,0,0);
}
