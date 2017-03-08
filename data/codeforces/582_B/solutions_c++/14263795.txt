#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const int maxn=303;
int a[maxn],dp[maxn],counts[maxn];
int main(){
	int n,t,maxCount=0,dpRes=0;
	scanf("%d%d",&n,&t);
	for(int i=0;i<n;i++){
		scanf("%d",a+i);
		counts[a[i]]++;
		maxCount=max(maxCount,counts[a[i]]);

	}
	for(int i=1;i<=min(t,n);i++){
		for(int j=0;j<n;j++){
			for(int k=a[j];k>=1;k--){
					dp[a[j]]=max(dp[a[j]],dp[k]+1);
					dpRes=max(dpRes,dp[a[j]]);
			}
		}
	}
	//printf("%d %d\n",dpRes,maxCount);
	printf("%d\n",dpRes+(t-min(t,n))*maxCount);
	return 0;
}