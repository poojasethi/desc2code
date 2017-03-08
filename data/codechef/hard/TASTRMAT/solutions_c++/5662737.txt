/*
   Nimesh Ghelani (nims11)
   */
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<stack>
#include<set>
#include<utility>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",a)
#define newline printf("\n")
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define P_I(a) printf("%d",a)

using namespace std;
int cnt = 0;
char str[100010], str2[100010];
int mod = 1000000007;
int POW(long long r, long long n)
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
long long pre[100010][2];
int getans(){
    int l = strlen(str2);
    int l2 = strlen(str);
    long long res = 0;
    int m = l2-l+1;
    for(int i = 0;str2[i];i++){
        int lt = i+(l2-l);
        int req = !(str2[i]-'0');
        long long foo = (pre[lt+1][req]-pre[i][req]+mod)%mod;
        long long bar= POW(100001, (l2-m)-i);
        bar = POW(bar, mod-2);
        foo = (foo*bar)%mod;
        res = (res + foo)%mod;
    }
    return res;
}
int main()
{
    in_S(str);
    int l = strlen(str);
    for(int i = 0;str[i];i++){
        int x = str[i]-'0';
        pre[i+1][x] = POW(100001, l-i-1);
        pre[i+1][0] = (pre[i+1][0]+pre[i][0])%mod;
        pre[i+1][1] = (pre[i+1][1]+pre[i][1])%mod;
    }
    int Q;
    in_I(Q);
    while(Q--){
        in_S(str2);
        printf("%d\n", getans());
    }
}
