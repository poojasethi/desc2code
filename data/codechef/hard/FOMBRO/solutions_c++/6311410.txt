/*
    Nimesh Ghelani (nims11)
*/
#include <bits/stdc++.h>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",a)
#define newline printf("\n")
#define BE(a) a.begin(), a.end()

using namespace std;
long long res[1000100];
int POW(long long r, long long n, int mod)
{
    int ans = 1;
    while(n>0)
    {
        if(n&1)
            ans = (ans*r)%mod;
        n >>= 1;
        r = (r*r)%mod;
    }
    return ans;
}
int main()
{
    in_T{
        int N, M, Q;
        in_I(N);
        in_I(M);
        in_I(Q);
        long long mod = M;
        res[1] = N;
        for(int i = 2;i<N;i++){
            res[1] = (res[1]*1LL*i)%M;
        }
        int num, den;
        long long cur;
        N++;
        if(N%2)
            num = N/2+1, den = N/2, cur = N/2+1;
        else
            num = N/2, den = N/2, cur = 1;
        N--;
        res[den] = cur;
        num++, den--;
        while(den>1){
            cur = (cur*(den+1))%mod;
            cur = (cur*num)%mod;
            res[den] = cur;
            num++, den--;
        }
        for(int i = 2;i<=N/2;i++)
            res[i] = (res[i]*res[i-1])%mod;
        while(Q--){
            int x;
            in_I(x);
            if(x > N/2)
                x = N - x;
            printf("%lld\n", res[x]);
        }
    }
}
