#include<bits/stdc++.h>
using namespace std;
int n;
int d[200005];
typedef long long LL;
LL A,sum;
int main(){
    scanf("%d%I64d",&n,&A);
    for(int i=1;i<=n;i++) scanf("%d",&d[i]),sum+=d[i];
    for(int i=1;i<=n;i++) printf("%I64d ",(d[i]-min((LL)d[i],A-n+1))+max(1LL,A-(sum-d[i]))-1);
    puts("");
    return 0;
}
