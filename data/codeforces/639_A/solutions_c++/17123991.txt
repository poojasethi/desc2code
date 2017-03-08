#include<bits/stdc++.h>
using namespace std;
const int max1 = 1e6 + 5;
int t[max1];
struct cmp{
	bool operator()(int a,int b){
		return t[a] < t[b];
	}
};
int main()
{
	int i,n,k,q;
	cin>>n>>k>>q;
	for(i=1;i<=n;i++)
	{
		cin>>t[i];
	}
	set<int, cmp> disp;
	while(q--)
	{
		int type,a;
		cin>>type>>a;
		if(type==1){
			disp.insert(a);
			if((int)disp.size() > k)
			disp.erase(disp.begin());
		}
		else
		{
			if(disp.find(a)==disp.end())
			cout<<"NO\n";
			else
			cout<<"YES\n";
		}
	}

return 0;
}
