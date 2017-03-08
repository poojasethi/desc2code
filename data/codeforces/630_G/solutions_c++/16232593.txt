#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
    ll n,ans;
    scanf("%lld",&n);
    ans=((n+4)/1*(n+3)/2*(n+2)/3*(n+1)/4*n/5)*((n+2)/1*(n+1)/2*n/3);
    printf("%lld\n",ans);
    return 0;
}
