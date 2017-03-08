#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=1e5+9;
ll a[N],b[N];
int n,k;
bool ok(ll x)
{
    ll num=k;
    for(int i=0;i<n;i++){
        ll t=b[i]-x*a[i];
        if(t<0){
            num+=t;
            if(num<0)return 0;
        }
    }
    return 1;
}
int main()
{
    scanf("%d%d",&n,&k);
    for(int i=0;i<n;i++)scanf("%I64d",&a[i]);
    for(int i=0;i<n;i++)scanf("%I64d",&b[i]);
    ll l=0,r=2e9+9;
    while(l<r){
        int m=l+(r-l+1)/2;
        if(ok(m))l=m;
        else r=m-1;
    }
    printf("%d\n",l);
}
