#include <bits/stdc++.h>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define PII pair<int,int>
#define VPII vector<pair<int,int> >
#define PLL pair<long long,long long>
#define F first
#define S second
typedef long long LL;
using namespace std;
const int SIZE = 1e6+10;
// template end here
int phi[5001];
int D[5002][5000],N,M,A[SIZE];
LL mypow(LL x,LL y,int mod){
    x%=mod;
    LL res=1%mod;
    while(y){
        if(y&1)res=res*x%mod;
        y>>=1;
        x=x*x%mod;
    }
    return res;
}
void pre(){
    REPP(i,1,5001){
        phi[i]=i;
    }
    REPP(i,2,5001){
        if(phi[i]==i){
            for(int j=i;j<5001;j+=i)phi[j]=phi[j]/i*(i-1);
        }
    }
}
int cnt[5000];
void f(int lv,int r,int mod){
    memset(D[lv],0,sizeof(int)*mod);
    if(mod==1){
        D[lv][0]=mypow(N,r,M);
        return;
    }
    if(r==1){
        REP(i,N)D[lv][A[i]%mod]++;
        REP(i,mod)D[lv][i]%=M;
        return;
    }
    f(lv+1,r-1,phi[mod]);
    memset(cnt,0,sizeof(int)*mod);
    REP(i,N)
        cnt[A[i]%mod]++;
    REP(i,mod)cnt[i]%=M;
    REP(i,mod){
        if(!cnt[i])continue;
        int now=mypow(i,phi[mod],mod);
        if(!i)now=0;
        REP(j,phi[mod]){
            D[lv][now]=(D[lv][now]+cnt[i]*D[lv+1][j])%M;
            now=now*i%mod;
        }
    }
}
int main(){
    pre();
    CASET{
        RII(N,M);
        REP(i,N)RI(A[i]);
        f(0,N,M);
        int an=0;
        REP(i,M)an=(an+D[0][i]*i)%M;
        printf("%d\n",an);
    }
    return 0;
}
 