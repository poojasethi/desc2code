#include <iostream>
#define DN 2000000
using namespace std;

int n,m,k,rez[DN],sz,lastDay,nextDay;

int main()
{
    cin>>n>>m>>k;
    if(k>1) {
        for(int i=1; i<=m+n; i+=n) for(int j=1; j<k; ++j)rez[++sz]=i;
        rez[++sz]=1;
        for(int i=n; i<=m+n; i+=n) rez[++sz]=i;
    }else {
        for(int lastDay=1;lastDay<=m+n;lastDay+=n-1) {
            rez[++sz]=lastDay;
        }
    }
    cout<<sz<<'\n';
    for(int i=1; i<=sz; ++i) cout<<rez[i]<<' ';
    return 0;
}
