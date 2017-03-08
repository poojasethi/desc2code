#include <bits/stdc++.h>

using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		int n,abz=0,sum=0,temp;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			if(temp>0)abz++;
			sum+=temp;
		}
		if(sum>=100&&sum-abz<100)cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
}