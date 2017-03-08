#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
  int k;
  string str, ps;
  cin>>str;
  cin>>k;
  int ans = 0;
  int c0, c1;
  for (int i = 0; i < k; i++) {
    cin>>ps;
    for (int j = 0; j < str.size(); j++) {
      c0 = 0;
      c1 = 0;
      while (j < str.size() && (str[j] == ps[0] || str[j] == ps[1])){
	(str[j] == ps[0])?c0++:c1++;
	j++;
      }
      ans += min(c0,c1);
    }
  }
  cout<<ans<<endl;
  return 0;
}
	
	
