#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <map>
#include <utility>
#include <set>

using namespace std;

#define CL(a, b) memset(a, b, sizeof(a))
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;

const int MAXN = 10000007;
const int MOD = 1000000007;

ll A[MAXN], RL[MAXN], RR[MAXN], F[MAXN];
ll N, Q, K;

struct qnode {
    ll idx, v;
    qnode(ll _idx, ll _v) { idx = _idx; v = _v; }
    bool operator < (const qnode & other) const {
        if(v == other.v) return idx < other.idx;
        else return v > other.v;
    }
};

void gen_Q() {
    ll a, b, c, d, e, f, r, s, t, m;
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld", &a, &b, &c, &d, &e, &f, &r, &s, &t, &m, &A[1]);
    ll tp = t;
    for(int x = 2; x <= N; x++) {
        tp = (tp * t) % s;
        ll ap = (A[x - 1] * A[x - 1]) % m;
        if(tp <= r)
            A[x] = (a * ap + b * A[x - 1] + c) % m;
        else
            A[x] = (d * ap + e * A[x - 1] + f) % m;
    }
}

void gen_LR() {
    ll L1, La, Lc, Lm, D1, Da, Dc, Dm;
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &L1, &La, &Lc, &Lm, &D1, &Da, &Dc, &Dm);
    for(int i = 1; i <= Q; i++) {
        L1 = (La * L1 + Lc) % Lm;
        D1 = (Da * D1 + Dc) % Dm;
        RL[i] = L1 + 1;
        RR[i] = min(RL[i] + K - 1 + D1, N);
    }
}

void prepare() {
    priority_queue<qnode> q;
    for(int i = N; i > 0; i--) {
        q.push(qnode(i, A[i]));
        while(q.top().idx - i + 1 > K) q.pop();
        F[i] = q.top().v;
    }
}

int main() {
    scanf("%lld %lld %lld", &N, &K, &Q);

    gen_Q(); gen_LR(); prepare();

    ll sum =0, prod = 1;
    for(int q = 1; q <= Q; q++) {
        ll l = RL[q], r = RR[q];
        ll res =min(F[l], F[r - K + 1]);
        sum += res;
        prod = (prod * res) % MOD;
    }
    printf("%lld %lld\n", sum, prod);
    return 0;
}

