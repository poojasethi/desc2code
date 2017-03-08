#include <iostream>
#include <queue>
#include <string>
using namespace std;
typedef pair<string,int> psi;
int main()
{
	string s;
	int k,i;
	psi t;
	priority_queue<psi,vector<psi>,greater<psi> > q;
	cin>>s>>k;
	if (k>(long long)s.size()*(s.size()+1)/2)
	{
		cout<<"No such line.";
		return 0;
	}
	for (i=0;i<s.size();i++)
		q.push(make_pair(s.substr(i,1),i));
	while (--k)
	{
		t=q.top();
		q.pop();
		if (t.second<s.size()-1)
		{
			t.first+=s[++t.second];
			q.push(t);
		}
	}
	t=q.top();
	cout<<t.first;
	return 0;
}
