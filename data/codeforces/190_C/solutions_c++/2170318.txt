#include<iostream>
#include<string>
#include<vector>
using namespace std;
bool valid;
string ans;
void cute()
{
  string s;
  if (cin>>s) {
    ans += s;
    if (s == "pair")
      ans += "<", cute(), ans += ",", cute(), ans += ">";
  } else
    valid = false;
}
int main()
{
  int n;
  cin>>n;
  valid = true;
  cute();
  string s;
  if (!valid || cin>>s)
    cout<<"Error occurred"<<endl;
  else
    cout<<ans<<endl;
  return 0;
}
