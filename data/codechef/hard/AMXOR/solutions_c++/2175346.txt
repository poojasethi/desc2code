#include <cstdio>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;


const ll MOD=1000000000+9;

int T, N;
ll mi[30];

pll ext_gcd(ll a, ll b)
{
    if (b == 0)
        return make_pair(1, 0);
    pll t = ext_gcd(b, a%b);
    ll x = t.first, y = t.second;
    return make_pair(y, x-(a/b)*y);
}

ll mod_inv(ll a)
{
    pll t = ext_gcd(a, MOD);
    ll ans = (t.first) % MOD;
    return (ans<0)? ans+MOD : ans;
}

void solve(vector<ll> &a)
{
    ll ans = 0;
    for(int k=29; k>=0; k--)
    {
        ll dp[2][2];
        dp[0][1] = 0, dp[0][0] = 1;
        ll ones=1, zeros=1;
        int p=1, M=0;
        for(int i=1; i<=N; i++)
        {
            //printf("a[i]=%lld\n", a[i]);
            if (a[i] & (1<<k))
            {
                M += 1;
                a[i] -= (1<<k);
                ones *= (a[i]+1);
                ones %= MOD;
                dp[p][1] = (dp[1-p][0]*(a[i]+1) + dp[1-p][1]*(1<<k))%MOD;
                dp[p][0] = (dp[1-p][1]*(a[i]+1) + dp[1-p][0]*(1<<k))%MOD;
            }
            else
            {
                zeros *= (a[i]+1);
                zeros %= MOD;
                dp[p][1] = (dp[1-p][1]*(a[i]+1))%MOD;
                dp[p][0] = (dp[1-p][0]*(a[i]+1))%MOD;
            }
            p = 1-p;
        }
        ans += (dp[1-p][M%2]+MOD-(ones*zeros)%MOD)*mi[k];
        ans %= MOD;
        
        //printf("dp=%lld, ones*zeros=%lld ans=%lld\n", dp[1-p][M%2], ones*zeros, ans);
    }
    printf("%lld\n", (ans+1)%MOD);
}

int main()
{
    for(int i=0; i<30; i++)
        mi[i] = mod_inv(1<<i);

    scanf("%d", &T);
    for(;T--;)
    {
        scanf("%d", &N);
        vector<ll> numbers(N+1);
        for(int i=1; i<=N; i++)
        {
            ll a;
            scanf("%lld", &a);
            numbers[i] = a;
        }
        solve(numbers);
    }    
    return 0;
}
