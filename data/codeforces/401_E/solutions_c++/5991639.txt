#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
using namespace std;

#define LL long long
#define mod 1000000007
#define MP make_pair
#define eps 1e-8
#define mxn 100005

LL n, m, L, R, p;
int f[mxn][10], cnt[mxn];

LL cal( LL ll, LL rr, LL mul ) {
    ll = (ll + mul - 1) / mul, rr = rr / mul;
    return (rr - ll + 1) * (m + 1) - (rr + ll) * (rr - ll + 1) / 2 * mul;
}

int main()
{
    cin >> n >> m >> L >> R >> p;
    for( int i = 2; i <= 100000; ++i )
        if( cnt[i] == 0 )
            for( int j = i; j <= 100000; j += i )
                f[j][cnt[j]++] = i;
    LL ans = 0, Min = L, Max = min(R, m), r = min(n, R);
    for( LL d = 1; d <= r; ++d ) {
        while( Min > 1 && (Min - 1) * (Min - 1) + d * d >= L * L ) --Min;
        while( Max * Max + d * d > R * R ) --Max;
        if( Min > Max ) continue;
        LL sum = 0;
        for( int i = 0; i < (1 << cnt[d]); ++i ) {
            LL mul = 1, fac = 1;
            for( int j = 0; j < cnt[d]; ++j )
                if( i >> j & 1 )
                    mul *= f[d][j], fac *= -1;
            sum += fac * cal(Min, Max, mul) % p;
        }
        ans = ((ans + sum * (n - d + 1)) % p + p) % p;
    }
    ans = ans * 2 % p;
    if( L == 1 ) ans = (ans + n * (m + 1) + (n + 1) * m) % p;
    cout << ans << endl;
    return 0;
}