#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<string,int> m;

string name;

void actualiza(string &name1,string &name2,int points)
{
  if (name1!=name) m[name1];
  if (name2!=name) m[name2];
  if (name1!=name) swap(name1,name2);
  if (name1!=name) return;
  m[name2]+=points;
}

int main()
{
  cin>>name;
  int n;
  cin>>n;
  for (int i=0;i<n;i++) {
    string name1;
    cin>>name1;
    string action;
    cin>>action;
    string on,name2,last;
    if (action=="posted") {
      cin>>on>>name2>>last;
      name2=name2.substr(0,int(name2.size())-2);
      actualiza(name1,name2,15);
    } else if (action=="commented") {
      cin>>on>>name2>>last;
      name2=name2.substr(0,int(name2.size())-2);
      actualiza(name1,name2,10);
    } else {
      cin>>name2>>last;
      name2=name2.substr(0,int(name2.size())-2);
      actualiza(name1,name2,5);
    }
  }
  vector<pair<int,string> > v;
  for (map<string,int>::iterator it=m.begin();it!=m.end();it++)
    v.push_back(pair<int,string> (-(it->second),it->first));
  sort(v.begin(),v.end());
  for (int i=0;i<int(v.size());i++)
    cout<<v[i].second<<endl;
}
