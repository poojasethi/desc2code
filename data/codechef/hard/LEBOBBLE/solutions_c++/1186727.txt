#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<map>
#include<cstring>
using namespace std;
long long bit[100001];
void update_bit(int idx, int x)
{
  for (; idx <= 100000; idx += (idx&-idx))
    bit[idx] += x;
}
long long read_bit(int idx)
{
  long long ret = 0;
  idx--;
  for (; idx > 0; idx -= (idx&-idx))
    ret += bit[idx];
  return ret;
}
long long B[50001], d;
int P[50001];
int n;

int main()
{
  int tests;
  scanf ("%d", &tests);
  while (tests--) {
    map<long long, int> pos;
    vector<long long> values;
    for (int i = 0; i <= 100000; i++) bit[i] = 0;
    scanf ("%d %Ld", &n, &d);
    for (int i = 0; i < n; i++)
      scanf ("%Ld", &B[i]);
    for (int i = 0; i < n; i++)
      scanf ("%d", &P[i]);
    for (int i = 0; i < n; i++) {
      values.push_back(B[i]);
      values.push_back(B[i] + d);
    }
    sort(values.begin(), values.end());
    int idx = 0;
    for (int i = values.size() - 1; i >= 0; i--)
      if (!pos[values[i]]) pos[values[i]] = ++idx;

    double ans = 0.0;
    for (int i = 0; i < n; i++) {
      ans += P[i]*read_bit(pos[B[i] + d]);
      ans += (100-P[i])*read_bit(pos[B[i]]);
      update_bit(pos[B[i] + d], P[i]);
      update_bit(pos[B[i]], 100-P[i]);
    }
    printf ("%.4lf\n", ans/10000.0);
  }
  return 0;
}
