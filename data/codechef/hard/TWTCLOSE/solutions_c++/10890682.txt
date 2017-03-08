#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n,k,opentweets=0;
	cin>>n>>k;
	vector<int> vec;
	vec.resize(n+1);
	string action;
	int action_no;
	for(int i=0;i<k;i++)
	{
		cin>>action;
		if(action=="CLICK")
		{
			cin>>action_no;
			if(vec[action_no]==0)
			{
				vec[action_no]=1;
				opentweets++;
			}
			else
			{
				vec[action_no]=0;
				opentweets--;
			}
		}
		else
		{
			for(int i=1;i<=n;i++)vec[i]=0;
				opentweets=0;
		}
		cout<<opentweets<<endl;
	}
}