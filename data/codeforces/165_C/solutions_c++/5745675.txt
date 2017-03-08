#include <iostream>
#include <string>
using namespace std;
long long cnt[1000001];
int main()
{
  long long k, ans;
  string str;
  cin>>k;
  cin>>str;
  ans = 0;
  int c = 0;
  cnt[0] = 1;
  for (int i = 0; i < str.size(); i++) {
    c += str[i] - '0';
    if (c >= k) ans += cnt[c - k];
    cnt[c]++;
  }
  cout<<ans<<endl;
  return 0;
}
