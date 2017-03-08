#include<bits/stdc++.h>
using namespace std;
int main()
{
	int v1,v2,t,d,sum=0;
	cin>>v1>>v2>>t>>d;
	sum = v1;
	for(int i = 1;i<=t - 2;i++)
	{
		sum+= min(v1 + i*d, v2 + (t-1)*d - i*d);
		
	}
	cout<<sum + v2;
	return 0;
}
