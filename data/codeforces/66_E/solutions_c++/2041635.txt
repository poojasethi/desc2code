#include<iostream>
#include<algorithm>
using namespace std;
int n, a[100001], b[100001];
bool can[100001];
int main()
{
  cin>>n;
  for (int i = 0; i < n; i++) cin>>a[i];
  for (int i = 0; i < n; i++) cin>>b[i];
  int mn = 0, sum = 0;
  for (int i = 0; i < n; i++) sum += a[i] - b[i], mn = min(mn, sum);
  if (mn == 0) can[0] = true;
  for (int i = 1; i < n; i++) {
    mn = min(0, mn - (a[i-1] - b[i-1]));
    if (mn == 0) can[i] = true;
  }
  rotate(b, b+n-1, b+n);
  mn = 0, sum = 0;
  for (int i = n-1; i >= 0; i--) sum += a[i] - b[i], mn = min(mn, sum);
  if (mn == 0) can[n-1] = true;
  for (int i = n-2; i >= 0; i--) {
    mn = min(0, mn - (a[i+1]-b[i+1]));
    if (mn == 0) can[i] = true;
  }
  int ans = 0;
  for (int i = 0; i <= n-1; i++) if (can[i]) ans++;
  cout<<ans<<endl;
  for (int i = 0; i <= n-1; i++) if (can[i]) cout<<i+1<<" ";cout<<endl;
  
  return 0;
}
