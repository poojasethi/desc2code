#include <iostream>

using namespace std;

string s;
int a=-1;
int main(){
  cin>>s;
  for(int i=0;i<s.size();i++){
    if((s[i]-'0')&1)
      continue;
    a=i;
    if(s[i]<s[s.length()-1])
      break;
  }
  if(a!=-1)
    swap(s[a],s[s.size()-1]);
  cout<<(a==-1?"-1":s)<<endl;
}
