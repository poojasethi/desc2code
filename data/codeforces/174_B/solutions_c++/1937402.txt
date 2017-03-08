#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
using namespace std;

int main()
{
  string str;
  cin>>str;
  vector<string> ans;
  bool flag = false;
  for (int i = 0; i < str.size(); i++) {
    int m, n;
    for (m = i; m < str.size(); m++) if (str[m] == '.') break;
    for (n = m + 1; n < str.size(); n++) if (str[n] == '.') break;
    if (m - i < 1 || m - i > 8) flag = true;
    if (n == str.size()) {
      if (n - m < 2 || n - m > 4) flag = true;
    } else {
      if (n - m <3 || n - m > 12) flag = true;
      if (n - m < 5) n = m + 2;
      else n = m + 4;
    }
    if (flag) break;
    ans.push_back(str.substr(i, n - i));
    i = n - 1;
  }
  if (flag)
    cout<<"NO"<<endl;
  else {
    cout<<"YES"<<endl;
    for (int i = 0; i < ans.size(); i++)
      cout<<ans[i]<<endl;
  }
  return 0;
}
