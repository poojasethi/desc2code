#include<bits/stdc++.h>
using namespace std;
int main()
{
	int N,M,t,p;
	cin>>N>>M;
	set< int > s;
	s.clear();
	while(N--)
	{
		cin>>t;
		while(t--)
		{
			cin>>p;
			s.insert(p);
		}
	}
	if(s.size()==M)
		cout<<"YES\n";
	else 
		cout<<"NO\n";
}
