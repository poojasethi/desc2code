#include <iostream>
#include <cmath>

using namespace std;

const int MAXN = 320000;

typedef long long LL;

LL a[MAXN], c[MAXN];

LL solve(LL n)
{
    int m = sqrt(0.9 + n);
    LL ret = 0;
    for(LL i = 1; i <= m; i++)
        a[i] = n / i - 1;
    for(int i = 1; i <= m; i++)
        c[i] = i - 1;
    LL s,t;
    for(LL p = 2; p <= m; p++)
    {
        if(c[p] == c[p - 1]) continue;
        s = n / (p * p);
        if(s > m) s = m;
        for(LL i = 2; i <= s; i++)
        {
            t = i * p;
            a[i] -= ((t <= m) ? a[t]:c[n/t]) - c[p - 1];
        }
        for(LL i = m, pp = p * p; i >= pp; i--)
            c[i] -= c[i/p] - c[p - 1];
    }
    for(int p = 2; p <= m; p++) if(c[p] != c[p - 1])
        ret += a[p] - c[p];
    return ret;
}

int main()
{
    LL n;
    cin >> n;
    int k = cbrt(0.9 + n);
    LL ans = solve(n) + c[k];
    cout << ans << endl;
    return 0;
}
