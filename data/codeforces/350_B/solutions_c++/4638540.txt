#include<bits/stdc++.h>
using namespace std;
int n,tp[100009],pr[100009],x,st[100009];
int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++)cin>>tp[i];
    for(int i=1;i<=n;i++)cin>>pr[i],st[pr[i]]++;
    vector < int > ans;
	for(int i=1;i<=n;i++)
	{
		if(tp[i]==1)
		{
		 	int curr=i;

		 	vector<int>cur;
		 	while (pr[curr]!=0&&st[pr[curr]]<=1)
		 	{
		 	 	cur.push_back(curr);
		 	 	curr=pr[curr];

		 	}
		 	cur.push_back(curr);
		 	if(ans.size()<cur.size())ans = cur;
		}
	}
	cout<<ans.size()<<"\n";
	reverse(ans.begin(),ans.end());
	for(int i=0;i<ans.size();i++)
	{
	    cout<<ans[i]<<" ";
	}
	cout<<"\n";
}

