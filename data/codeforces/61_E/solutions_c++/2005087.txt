#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
long long bit[2][1000001];
long long bit_read(int idx, int k)
{
  long long x = 0;
  for (; idx; idx -= idx&-idx)
    x += bit[k][idx];
  return x;
}
void bit_update(int idx, int val, int k)
{
  for (;idx <= 1000000; idx += (idx&-idx))
    bit[k][idx] += val;
}
int a[1000001], b[1000001];
int n;
map<int, int> btoa;
int main()
{
  cin>>n;
  for (int i = 0; i < n; i++) {cin>>b[i]; a[i+1] = b[i];}
  sort(b, b + n);
  for (int i = 0; i < n; i++) btoa[b[i]] = i+1;
  for (int i = 1; i <= n; i++) a[i] = btoa[a[i]];

  long long ans = 0;
  for (int i = n; i > 0; i--) {
      long long x = bit_read(a[i]-1, 0);
      bit_update(a[i], 1, 0);
      bit_update(a[i], x, 1);
      ans += bit_read(a[i]-1, 1);
  }
  cout<<ans<<endl;
  return 0;
}
