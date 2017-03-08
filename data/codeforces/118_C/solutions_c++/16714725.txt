#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,k,p,c,res=1e9;
	string s,t,ans;
	cin>>n>>k>>s;
	for (int i=0;i<10;i++)
	{
		t=s,p=k,c=0;
		for (int j=0;j<10;j++)
		{
			for (int l=0;l<n;l++)
				if (p && t[l]-48==i+j)
					p--,t[l]=i+48,c+=j;
			if (j)
				for (int l=n-1;l>=0;l--)
					if (p&& t[l]-48==i-j)
						p--,t[l]=i+48,c+=j;
		}
		if (c<res) res=c,ans=t;
		if (c==res) ans=min(ans,t);	
	}
	cout<<res<<endl<<ans;
}