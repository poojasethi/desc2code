#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int pos[6][1003];
int a[6][1003];
int dp[1003];
int N, K;
int main(){
	scanf("%d%d", &N, &K);
	for(int i=1;i<=K;++i){
		for(int j=1;j<=N;++j){
			scanf("%d", &a[i][j]);
			pos[i][a[i][j]] = j;
		}
	}
	int ans = 1;
	dp[N] = 1;
	for(int i=N-1;i>=1;--i){
		dp[i] = 1;
		for(int j=i+1;j<=N;++j){
			bool ok = true;
			for(int k=1;k<=K;++k){
				if(pos[k][a[1][i]] > pos[k][a[1][j]]){
					ok = false;
					break;
				}
			}
			if(ok){
				dp[i] = max(dp[i], 1+dp[j]);
			}
		}
		ans = max(ans, dp[i]);
	}
	printf("%d\n",ans);
	return 0;
}