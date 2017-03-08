#include <bits/stdc++.h>

using namespace std;

#define NMAX 10010
#define MMAX 10010
#define KMAX 128

int n, m, k;
int s1, s2, f;

typedef unsigned long long ll;

struct edge {
  int u, v;
  int w;
  int l, r;
};

struct vertex {
  int v;
  ll d;
  bool operator < (const vertex &o) const {
    return d > o.d;
  }
};

edge E[MMAX+KMAX];
vector <int> G[NMAX];
ll D1[NMAX], D2[NMAX];

void dijkstra(int s, ll *D) {
  memset(D, -1, sizeof(ll) * NMAX);
  D[s] = 0;
  priority_queue <vertex> Q;
  Q.push((vertex) {s, 0});
  while (!Q.empty()) {
    vertex u = Q.top();
    Q.pop();
    if (u.d != D[u.v]) {
      continue;
    }
    for (int i = 0; i < G[u.v].size(); i++) {
      edge e = E[G[u.v][i]];
      vertex v = {e.v, u.d + (ll) e.w};
      if (v.d < D[v.v]) {
        D[v.v] = v.d;
        Q.push(v);
      }
    }
  }
}

void print_output() {
  for (int i = 0; i < k; i++) {
    printf("%d ", E[m+i].w);
  }
  printf("\n");
}

int loop(int draw) {
  int changed;
  do {
    dijkstra(s1, D1);
    dijkstra(s2, D2);

    int cmp = draw ? (D1[f] <= D2[f]) : (D1[f] < D2[f]);
    if (cmp) {
      return 1;
    }

    changed = 0;
    for (int i = 0; i < k; i++) {
      int u = E[m+i].u;
      int v = E[m+i].v;
      int w = E[m+i].w;
      int l = E[m+i].l;
      int cmp = draw ? (D1[u] <= D2[u]) : (D1[u] < D2[u]);
      if (cmp && l < w) {
        E[m+i].w = l;
        changed = 1;
      }
    }
  } while (changed);

  return 0;
}

int main() {
  scanf("%d %d %d", &n, &m, &k);
  scanf("%d %d %d", &s1, &s2, &f);
  for (int i = 0; i < m; i++) {
    int u, v, w;
    scanf("%d %d %d", &u, &v, &w);
    E[i] = (edge) { u, v, w, w, w };
    G[u].push_back(i);
  }
  for (int i = 0; i < k; i++) {
    int u, v, l, r;
    scanf("%d %d %d %d", &u, &v, &l, &r);
    E[m+i] = (edge) { u, v, r, l, r };
    G[u].push_back(m+i);
  }

  if (loop(0)) {
    printf("WIN\n");
    print_output();
  } else if (loop(1)) {
    printf("DRAW\n");
    print_output();
  } else {
    printf("LOSE\n");
  }
  return 0;
}
