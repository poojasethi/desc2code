#include <iostream>
#define DN 100005
using namespace std;

int n,k,mc,d[DN],s[DN];

int main()
{
    cin>>n>>k;
    for(int i=1; i<=n; ++i) cin>>d[i];
    for(int i=1; i<=n; ++i) cin>>s[i];
    int cc=0,tt=0;
    for(int i=1; i<=n; ++i) {
        cc+=s[i];
        mc=max(mc,s[i]);
        for(;cc<d[i];cc+=mc,tt+=k);
        tt+=d[i];
        cc-=d[i];
    }
    cout<<tt;
    return 0;
}
