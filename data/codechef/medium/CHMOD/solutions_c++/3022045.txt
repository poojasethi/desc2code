#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
vector<int>prime;
#define maxn 100010
int dp[maxn][26];
int vis[101];
long long Pow(long long a,long long b,long long mod){
    long long ans=1;
    while(b){
        if(b&1) b--,ans=(ans*a)%mod;
        else b/=2,a=(a*a)%mod;
    }
    return ans;
}
int main(){
    memset(vis,1,sizeof(vis));
    prime.clear();
    for(int i=2;i<101;i++){
        if(vis[i]){
            prime.push_back(i);
            for(int j=2*i;j<101;j+=i) vis[j]=0;
        }
    }
    int n,x;
    scanf("%d",&n);
    memset(dp,0,sizeof(dp));
    for(int i=1;i<=n;i++){
        scanf("%d",&x);
        for(int j=0;j<prime.size()&&prime[j]<=x;j++){
            while(x%prime[j]==0){
                x/=prime[j];
                dp[i][j]++;
            }
        }
    }
    for(int i=1;i<=n;i++){
        for(int j=0;j<prime.size();j++)
            dp[i][j]+=dp[i-1][j];
    }
    int T;
    scanf("%d",&T);
    while(T--){
        int x,y,z;
        long long ans=1;
        scanf("%d%d%d",&x,&y,&z);
        for(int i=0;i<prime.size();i++){
            ans=(ans*Pow(prime[i],dp[y][i]-dp[x-1][i],z))%z;
        }
        printf("%lld\n",ans);
    }
    return 0;
}
