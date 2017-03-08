/*
 * PROB: Codeforces - 513E1 - Subarray Cuts
 * LANG: C++
 */

#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for(int i=int(a),n##i=int(b);i<=n##i;i++)
#define ms(f,a) memset(f,a,sizeof f)
#define SZ 405
#define INF 0x3f3f3f3f

typedef long long ll;

int f[51][SZ][SZ],h[SZ],a[SZ],N,K;

int main(void) {
#ifndef ONLINE_JUDGE
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    while(cin>>N>>K) {
        ms(h,0),ms(f,0);
        rep(i,1,N) cin>>a[i],h[i]=h[i-1]+a[i];
        rep(a,2,50)rep(b,0,N)rep(c,0,N) f[a][b][c]=-INF;
        rep(k,2,K) {
            rep(a,k,N)rep(b,k,a)rep(c,k-1,b-1) {
                f[k][b][a]=max(f[k][b][a],f[k-1][c][b-1]+(int)abs(h[c-1]-2*h[b-1]+h[a]));
            }
        }
        int ans=-INF;
        rep(x,1,N)rep(y,x,N) ans=max(ans,f[K][x][y]);
        cout<<ans<<endl;
    }
    return 0;
}
