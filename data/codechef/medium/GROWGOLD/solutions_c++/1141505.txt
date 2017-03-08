#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#define FOR(a,b,c) for (int a=b;a<=c;a++)
#define FORD(a,b,c) for (int a=b;a>=c;a--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define REPD(i,a) for(int i=(a)-1; i>=0; --i)
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007
#define dMod 100000007

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii,int> iii;

const int maxn=107;
struct matrix{ll a[maxn][maxn];};

int T,initTax,slot1,slot2,K,N,f[maxn];

matrix nhan(const matrix &a, const matrix &b){
    matrix res;
    FOR(i,1,K) FOR(j,1,K){
        ll s=0;
        FOR(z,1,K) s+=a.a[i][z]*b.a[z][j];
        res.a[i][j]=s%(dMod-1);
    }
    return res;
}

matrix pow_vii(ll n){
    matrix mat,mul;
    reset(mat.a,0); reset(mul.a,0);
    FOR(i,1,K-1) mat.a[i][i+1]=1;
    FOR(i,1,K) mat.a[K][i]=mul.a[i][i]=1;
    while(n){
        if(n&1) mul=nhan(mat,mul);
        mat=nhan(mat,mat);
        n>>=1;
    }
    return mul;
}

ll pow_ll(const ll &a, ll n){
    if(n==1) return a;
    ll t=pow_ll(a,n/2);
    if(n&1) return((((t*t)%dMod)*a)%dMod); else return((t*t)%dMod);
}

//#include <conio.h>
int main(){
    //freopen("test.txt","r",stdin);
    cin>>T;
    REP(index,T){
        cin>>initTax>>slot1>>slot2>>K>>N;
        f[1]=initTax;
        FOR(i,2,slot1+1) f[i]=f[i-1]+1;
        FOR(i,slot1+2,slot1+slot2+1) f[i]=(f[i-1]*2)%dMod;
        if(N<=slot1+slot2+1) cout<<f[N]<<endl;
        else if(K==1) cout<<f[slot1+slot2+1]<<endl;
        else{
            matrix ans=pow_vii(N-slot1-slot2-1);
            ll res=1;
            for(int i=slot1+slot2+1-K+1, j=1; j<=K; i++, j++) res=(res*pow_ll(f[i],ans.a[K][j]))%dMod;
            cout<<res<<endl;
        }
    }
    //getch();
    return 0;
}
