#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string str;
vector<string> b;
int main()
{
  int n;
  cin>>str;
  cin>>n;
  b.resize(n + 1);
  for (int i = 1; i <= n; i++)
    cin>>b[i];
  int maxLen = 0, maxPos = 0;
  int pos = 0;
  for (int i = 0; i < str.size(); i++) {
    for (int j = 1; j <= n; j++) if (b[j].size() <= i + 1) {
	if (str.substr(i - b[j].size() + 1, b[j].size()) == b[j]) 
	  pos = max(pos, i - (int)b[j].size() + 2);
      }
    int len = i - pos + 1;
    if (len > maxLen) maxLen = len, maxPos = pos;
  }
  cout<<maxLen<<" "<<maxPos<<endl;
  return 0;
}
