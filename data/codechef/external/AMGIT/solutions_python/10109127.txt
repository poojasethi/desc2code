#include <bits/stdc++.h>

using namespace std;

#define mem(a, v) memset(a, v, sizeof (a))
#define x first
#define y second
#define all(a) (a).begin(), (a).end()
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define rep(i, n) for (int i = 0; i < int(n); i ++)
#define repi(i, a, n) for (int i = (a); i < int(n); i ++)
#define repe(x, v) for (auto x: (v))

vector <int> adj[10005];
int L[10005];
int dp[100005][2];

int solve(int u, int f) {
    if (dp[u][f] != -1) {
        return dp[u][f];
    }
    if (L[u] != -1) {
        return L[u] != f;
    }
    int c = 0, d = 0;
    repe(v, adj[u]) {
        c += solve(v, f);
        d += solve(v, f^1);
    }
    return dp[u][f] = min(c, d+1);
}

map <string, int> node;
int z;
map <pair <int, int>, bool> edge;

void process(string s, int f) {
    string p = "/";
    int parent = node[p];
    for (int i = 1; i < sz(s); i ++) {
        while (i < sz(s)) {
            p.pb(s[i]);
            if (s[i] == '/') {
                break;
            }
            i ++;
        }
        if (!node.count(p)) {
            node[p] = z ++;
        }
        int child = node[p];
        if (!edge.count(mp(parent, child))) {
            adj[parent].pb(child);
            edge[mp(parent, child)] = true;
        }
        parent = child;
    }
    L[parent] = f;
}

int main () {
    std::ios_base::sync_with_stdio(false);
    int tst;
    cin >> tst;
    while (tst --) {
        z = 0;
        node.clear();
        edge.clear();
        mem(L, -1);
        rep(i, 10005) {
            adj[i].clear();
        }
        int n;
        cin >> n;
        node["/"] = z++;
        rep(i, n) {
            string p, q;
            cin >> p >> q;
            process(q, p == "stage");
        }
        mem(dp, -1);
        cout << solve(node["/"], 0) << "\n";
    }
    return 0;
}
