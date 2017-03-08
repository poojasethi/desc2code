#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 1e5+100;
int v[maxn], p[maxn];
vector<int> e[maxn];
int n, q;

void dfs(int x, int cp) {
    p[x] = cp;
    for (int i = 0; i < e[x].size(); i++)
        if (e[x][i] != cp)
            dfs(e[x][i], x);
}

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int gao(int x) {
    for (int cp = p[x]; cp != -1; cp = p[cp]) {
        if (gcd(v[x], v[cp]) > 1)
            return cp;
    }
    return -1;
}

int main(){
    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    for (int i = 0; i < n - 1; i++) {
        int j , k;
        cin >> j >> k;
        e[j].push_back(k);
        e[k].push_back(j);
    }
    dfs(1, -1);

    while (q--) {
        int t, x, a, b;
        cin >> t;
        if (t == 1) {
            cin >> x;
            int ans = gao(x);
            cout << ans << endl;
        }else {
            cin >> a >> b;
            v[a] = b;
        }
    }
    return 0;
}
