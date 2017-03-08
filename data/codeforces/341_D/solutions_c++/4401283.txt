#include <iostream>
#define zeros(x) (((x)^(x-1))&(x))
#define LL long long
using namespace std;

LL n,m,aib[2][2][1005][1005];

void up(int x,int y, LL v) {
    for(int i=x; i<=n; i+=zeros(i)) for(int j=y; j<=n; j+=zeros(j)) {
        aib[x&1][y&1][i][j]^=v;
        //cerr<<i<<' '<<j<<'\n';
    }
}

LL sum(int x,int y) {
    LL r=0;
    for(int i=x;0<i;i-=zeros(i)) for(int j=y;0<j;j-=zeros(j)) {
      //cerr<<i<<' '<<j<<'\n';
      r^=aib[x&1][y&1][i][j];
    }
    return r;
}

int main()
{
    int op,x1,y1,x2,y2;LL vl;
    for(cin>>n>>m;m;--m) {
      cin>>op;
        if(1==op) {
            cin>>x1>>y1>>x2>>y2;
            cout<<(sum(x2,y2)^sum(x2,y1-1)^sum(x1-1,y2)^sum(x1-1,y1-1))<<'\n';
        }else {
            cin>>x1>>y1>>x2>>y2>>vl;
            up(x2+1,y2+1,vl); up(x2+1,y1,vl); up(x1,y2+1,vl); up(x1,y1,vl);
        }
    }
    return 0;
}
