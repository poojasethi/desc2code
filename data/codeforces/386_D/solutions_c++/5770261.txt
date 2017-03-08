#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

char adj[77][77]; int trfr[567890], trt[567890], d[567890], pth[567890][2];
queue<int> q;
int main() {
    int n, a, b, c, st, ta, tb, tc, tr;

    scanf("%d %d %d %d", &n, &a, &b, &c); a--; b--; c--;
    for (int i = 0; i < n; i++) scanf("%s", adj+i);
    if (a>b) swap(a, b); if (b>c) swap(b, c); if (a>b) swap(a, b);
    st = n*n*a + n*b + c; trt[st] = -1; q.push(st);
    while (!q.empty()) {
        int pop = q.front(); q.pop();
        if (pop == n + 2) break;
        int pa = (pop/n)/n, pb = (pop-n*n*pa)/n, pc = pop-n*n*pa-n*pb, pd = d[pop];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < n; j++) if (j!=pa && j!=pb && j!=pc && adj[j][pa] == adj[pb][pc]) {
                int na = j, nb = pb, nc = pc;
                if (na>nb) swap(na, nb); if (nb>nc) swap(nb, nc); if (na>nb) swap(na, nb);
                int psh = n*n*na + n*nb + nc;
                if (!trt[psh] && !trfr[psh]) {
                    trfr[psh] = pa; trt[psh] = j; d[psh] = pd+1; q.push(psh);
                }
            }
            int t = pa; pa = pb; pb = pc; pc = t;
        }
    }
    if (!trt[n+2] && !trfr[n+2]) {
        printf("-1\n"); return 0;
    }
    printf("%d\n", d[n+2]); ta = 0; tb = 1; tc = 2;
    for (int i = d[n+2]-1; i >= 0; i--) {
        tr = n*n*ta + n*tb + tc;
        pth[i][0] = trfr[tr]; pth[i][1] = trt[tr];
        if (ta == trt[tr]) ta = trfr[tr];
        else if (tb == trt[tr]) tb = trfr[tr];
        else tc = trfr[tr];
        if (ta>tb) swap(ta, tb); if (tb>tc) swap(tb, tc); if (ta>tb) swap(ta, tb);
    }
    for (int i = 0; i < d[n+2]; i++) printf("%d %d\n", pth[i][0]+1, pth[i][1]+1);

    return 0;
}