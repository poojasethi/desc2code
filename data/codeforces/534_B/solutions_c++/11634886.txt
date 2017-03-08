#include<bits/stdc++.h>
using namespace std;

int main()
{
	int i,v1,v2,t,d;
	int sum;
	
	cin>>v1>>v2;
	cin>>t>>d;
	
	sum=v1+v2;
	
	for(i=1;i<=t-2;i++)
	{
		sum+=min(v1+d*i,v2+(t-i-1)*d);
	}
	
	cout<<sum;
	return 0;
}
