#include<bits/stdc++.h>

using namespace std;


vector<int> getsubsets(vector<int> ms, int x)
{
	int vsize=ms.size();
	for(int i=0;i<vsize;i++)
	{
		ms.push_back(x+ms[i]);
	}
	return ms;
}

int main()
{
	map<int,int> mp;
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,var;
		cin>>n;
		int ssize=int(pow(2,n));
		for(int j=0;j<ssize;j++)
		{
			cin>>var;
			if(mp.find(var)==mp.end())mp[var]=1;
			else mp[var]++;
		}
		vector<int> ans;
		ans.resize(0);
		vector<int> ss;
		ss.push_back(0);
		for(int j=0;j<n;j++)
		{
			map<int,int>::iterator it = mp.begin();
			it++;
			//cout<<it->first<<endl;
			ss=getsubsets(ss,it->first);
			ans.push_back(it->first);
			for(int j=ss.size()/2;j<ss.size();j++)
			{
				mp[ss[j]]--;
				if(mp[ss[j]]==0)mp.erase(ss[j]);
			}
			cout<<ans[j]<<" ";
		}
		cout<<endl;

	}
}