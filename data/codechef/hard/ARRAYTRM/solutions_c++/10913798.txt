#include <bits/stdc++.h>

using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,k;
		cin>>n>>k;
		vector<int> vec;
		vector<int> groups;
		groups.resize(k+1);
		vec.resize(n);
		for(int i=0;i<n;i++)
		{
			cin>>vec[i];
			groups[vec[i]%(k+1)]++;
		}
		int count=0;
		vector<int> res;
		for(int i=0;i<groups.size();i++)if(groups[i]>0){res.push_back(groups[i]);}
		if(res.size()>2)
		{
			cout<<"NO"<<endl;
		}
		else if(res.size()==1)
		{
			cout<<"YES"<<endl;
		}
		else if(res[0]>1&&res[1]>1)
		{
			cout<<"NO"<<endl;
		}
		else cout<<"YES"<<endl;

	}
}