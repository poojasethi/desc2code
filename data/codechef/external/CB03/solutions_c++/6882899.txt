#include <bits/stdc++.h>
#define M 1000000007
#define lli long long

using namespace std;

string s;
lli dp[102][102];

lli f(int left, int right)
{
    if ( left > right ) return 0;
    if ( left == right ) return 1;
    lli &ans = dp[left][right];
    if ( ans != -1 ) return ans;
    ans = f(left,right-1) + f(left+1,right) - f(left+1,right-1);
    if ( s[left] == s[right] ) ans += 1 + f(left+1,right-1);
    return ans;
}

int main()
{
    int t;
    cin >> t;
    while ( t-- ) {
        cin >> s;
        int n = (int)s.size();
        memset(dp, -1, sizeof(dp));
        lli ans = f(0,n-1);
        cout << ans << endl;
    }
    return 0;
}
