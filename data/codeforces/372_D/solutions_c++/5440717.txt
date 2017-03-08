#include <cstdio>
#include <cstring>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int N, K, lg;
int ans = 0;
int E=0, e[222222], nxt[222222], fst[111111];
int dep[111111], anc[111111][20];
int s[111111], pos[111111], cnt=0;

void ae(int u, int v) {
    e[E] = v;
    nxt[E] = fst[u];
    fst[u] = E++;
}

void dfs(int u, int p, int d) {
    anc[u][0] = p;
    dep[u] = d;
    s[cnt] = u;
    pos[u] = cnt++;
    for (int i = 1; i < lg; ++i)
        anc[u][i] = anc[u][i-1] ? anc[anc[u][i-1]][i-1] : 0;
    for (int i = fst[u]; ~i; i = nxt[i])
        if (e[i] != p)
            dfs(e[i], u, d+1);
}

int lca(int u, int v) {
    if (dep[u] < dep[v])
        swap(u, v);
    for (int i=0, d=dep[u]-dep[v]; i<lg && d; ++i, d>>=1)
        if (d&1) u = anc[u][i];
    if (u == v) return u;
    for (int i = lg-1; i >= 0; --i)
        if (anc[u][i] != anc[v][i]) {
            u = anc[u][i];
            v = anc[v][i];
        }
    return anc[u][0];
}

set<int> homura;

int cost(int u) {
    if (homura.empty()) return 1;
    set<int>::iterator it = homura.lower_bound(pos[u]);
    int r = s[it==homura.end() ? *homura.begin() : *it];
    int l = s[it==homura.begin() ? *homura.rbegin(): *(--it)];
    return dep[u]-dep[lca(u, l)]-dep[lca(u, r)]+dep[lca(l, r)];
}

int main() {
    int i, j, k;
    memset(fst, -1, sizeof fst);
    cin>>N>>K;
    int tmp = N;
    for (lg=0; tmp; lg++, tmp>>=1);
    for (i = 1; i < N; ++i) {
        cin>>j>>k;
        ae(j, k); ae(k, j);
    }
    dfs(1, 0, 0);
    int size = 0;
    ans = 0;
    for (i = j = 1; i <= N; ++i) {//[i, j)
        for (; size<=K; ++j) {
            ans = max(ans, j-i);
            if (j > N) break;
            size += cost(j);
            homura.insert(pos[j]);
        }
        homura.erase(pos[i]);
        size -= cost(i);
    }
    cout<<ans<<endl;
    return 0;
}
