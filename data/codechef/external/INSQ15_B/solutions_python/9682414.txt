#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const double eps = 1e-9;
const int inf = 1000000000;
////////////////0123456789
const int MAX = 204;
const int modn = 1000000007;

int mdp[MAX][MAX], mdp_aim[MAX][MAX];
pii city[MAX];
int n;

int aim (int i, int j) {
    if (mdp_aim[i][j] != -1) 
        return mdp_aim[i][j];
    int ans = 0;
    for (int k = i+1; k < j; k++)
        ans += min (city[k].ff - city[i].ff + city[i].ss,
                city[j].ff - city[k].ff + city[j].ss);
    return mdp_aim[i][j] = ans;
}

int dp (int i, int k) {
    if (k == 0) {
        int r = 0;
        for (int j = i+1; j < n; j++)
            r += city[j].ff - city[i].ff + city[i].ss;
        return r;
    }
    if (i == n-1) return inf;
    if (mdp[i][k] != -1) return mdp[i][k];
    int ans = inf;
    for (int j = i+1; j < n; j++)
        ans = min (ans, aim (i, j) + dp (j, k-1));
    return mdp[i][k] = ans;
}

int main() {
    int t, k, sum, ans;
    scanf (" %d", &t);
    while (t--) {
        scanf (" %d %d", &n, &k);
        memset (mdp, -1, sizeof mdp);
        memset (mdp_aim, -1, sizeof mdp_aim);
        for (int i = 0; i < n; i++)
            scanf (" %d", &city[i].ff);
        for (int i = 0; i < n; i++)
            scanf (" %d", &city[i].ss);
        sort (city, city + n);
        ans = inf;
        for (int i = 0; i < n; i++) {
            sum = 0;
            for (int j = 0; j < i; j++)
                sum += city[i].ff - city[j].ff + city[i].ss;
            ans = min (ans, sum + dp (i, k-1));
        }
        printf ("%d\n", ans);
    }
}

