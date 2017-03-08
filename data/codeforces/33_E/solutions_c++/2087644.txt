#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int MDAY = 24 * 60, END = 30 * 24 * 60, N = 105, SL = 35;

int n, m, k, t1, t2, st[N], last, top, f[END], g[END], s[N], w[N], t[N], d[N], l[N], ord[N], c[N][END], pre[N][END], ans, ansts[N], anste[N], stack[N];
char sn[N][SL], tmp[SL];
bool used[MDAY];

int time_mins(const char *t, const int i) {
  int hours = (t[i] - '0') * 10 + (t[i + 1] - '0'), mins = (t[i + 3] - '0') * 10 + (t[i + 4] - '0');
  return hours * 60 + mins;
}

void print_time(const int m) {
  int days = m / MDAY + 1, hours = m % MDAY / 60, mins = m % MDAY % 60;
  printf("%d %d%d:%d%d", days, hours / 10, hours % 10, mins / 10, mins % 10);
}

bool cmp(int i, int j) {return l[i] < l[j];}

int main() {
  scanf("%d %d %d", &m, &n, &k);
  int tl;
  for (int i = 1; i <= m; ++i) scanf("%s", &sn[i]);
  for (int i = 1; i <= m; ++i) scanf("%d", &st[i]);
  for (int i = 1; i <= 4; ++i) {
    scanf("%s", tmp);
    int tstart = time_mins(tmp, 0), tend = time_mins(tmp, 6);
    for (int j = tstart; j <= tend; ++j) used[j] = true;
  }
  last = k * 24 * 60;
  top = 0;
  for (int i = 0; i < last; ++i) {
    if (!used[i % MDAY]) f[++top] = i;
    g[i] = top;
  }
  for (int i = 1; i <= n; ++i) {
    scanf("%s", &tmp);
    for (int j = 1; j <= m; ++j) if (strcmp(tmp, sn[j]) == 0) s[i] = j;
    scanf("%d %s %d", &t1, &tmp, &w[i]);
    t[i] = (t1 - 1) * MDAY + time_mins(tmp, 0);
    d[i] = s[i] == 0 ? -1 : g[used[t[i] % MDAY] ? t[i] : t[i] - 1] - st[s[i]] + 1;
    l[i] = s[i] == 0 ? -1 : g[used[t[i] % MDAY] ? t[i] : t[i] - 1];
    ord[i] = i;
  }
  sort(ord + 1, ord + n + 1, cmp);
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j <= top; ++j) {
      c[i][j] = c[i - 1][j];
      pre[i][j] = c[i][j] ? -1 : 0;
    }
    for (int j = 0; j < d[ord[i]]; ++j) {
      if (c[i][j + st[s[ord[i]]]] < c[i - 1][j] + w[ord[i]]) {
        c[i][j + st[s[ord[i]]]] = c[i - 1][j] + w[ord[i]];
        pre[i][j + st[s[ord[i]]]] = 1;
      }
    }
  }
  ans = 0;
  for (int i = 1; i <= top; ++i) {
    if (c[n][i] > c[n][ans]) ans = i;
  }
  
  printf("%d\n", c[n][ans]);
  int stop = 0, ti = n, tj = ans;
  while (pre[ti][tj] == -1) --ti;
  while (pre[ti][tj]) {
    ++stop;
    anste[stop] = f[tj];
    stack[stop] = ord[ti];
    tj -= st[s[ord[ti]]]; --ti;
    ansts[stop] = f[tj + 1];
    while (pre[ti][tj] == -1) --ti;
  }
  printf("%d\n", stop);
  for (int i = stop; i > 0; --i) {
    printf("%d ", stack[i]);
    print_time(ansts[i]);
    printf(" ");
    print_time(anste[i]);
    printf("\n");
  }  
  return 0;
}
