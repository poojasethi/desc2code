#include <iostream>
#include <string>
#include <set>
using namespace std;
 
main() {
  int cases;
  cin>>cases;
  while(cases--){
    string s, t;
    cin>>s>>t;
    set<char> S(s.begin(),s.end());
    int cnt = 0;
    for(int i=0;i<t.size();i++) if(S.count(t[i])) cnt++;
    cout<<cnt<<endl;
  }
}
