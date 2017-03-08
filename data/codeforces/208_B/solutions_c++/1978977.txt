#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;
typedef vector<string> vs;
set< vs > states;
bool solve (vs x)
{
  if (x.size() == 1) return true;
  bool ok = false;
  if (!states.insert(x).second) return false;
  int n = x.size() - 1;
  if (x[n][0] == x[n-1][0] || x[n][1] == x[n-1][1]) {
    vs nx(x.begin(), x.end() - 1);
    nx[n-1] = x[n];
    ok = solve(nx);
  }
  if (!ok && x.size() >= 4 && (x[n][0] == x[n-3][0] || x[n][1] == x[n-3][1])) {
    vs nx(x.begin(), x.end() - 1);
    nx[n-3] = x[n];
    ok = solve(nx);
  }
  return ok;
}
int main()
{
  int n;
  cin>>n;
  vs inp(n);
  for (int i = 0; i < n; i++) {
    cin>>inp[i];
  }
  cout<<(solve(inp)?"YES":"NO");
  cout<<endl;
  return 0;
}
