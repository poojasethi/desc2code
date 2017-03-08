#include<iostream>
#include<string>
using namespace std;
string num;
int n;
char ans[100001];
bool solve(int k, int c4, int c7, bool g)
{
  if (k == n) {
    for (int i = 0; i < n; i++) cout<<ans[i];cout<<endl;
    return true;
  }
  bool ret = false;
  if (c4 > 0 && (num[k] <= '4' || g)) {
    ans[k] = '4';
    ret |= solve(k+1, c4-1, c7, g | (num[k]<'4'));
  }
  if (!ret) {
    if (c7 > 0 && (num[k] <= '7' || g)) {
      ans[k] = '7';
      ret |= solve(k+1, c4, c7-1, g | (num[k]<'7'));
    }
  }
  return ret;
}
bool solve2(int k)
{
  if (k%2) return false;
  if (k > n) {
    for (int i = 0; i < k/2; i++) cout<<"4";
    for (int i = k/2; i < k; i++) cout<<"7"; cout<<endl;
    return true;
  }
  return solve(0, n/2, n/2, 0);
}
int main()
{
  cin>>num;
  bool ok = true;
  n = num.size();
  (solve2(n) || solve2(n+1) || solve2(n+2));
  return 0;
}
