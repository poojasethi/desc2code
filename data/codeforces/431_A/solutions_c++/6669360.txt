#include <bits/stdc++.h>

using namespace std;

int main(){
  int a[4];
  cin>>a[0]>>a[1]>>a[2]>>a[3];
  string s;
  cin>>s;
  long long sol=0;
  for(int i=0;i<s.size();i++)
    sol+=a[s[i]-'1'];
  cout<<sol<<endl;
}


