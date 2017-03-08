#include<bits/stdc++.h>
#define LL long long int
using namespace std;
int main()
{
	LL n,i;
	cin>>n;
	map<LL,int>d;
	LL sum=0,ans=n-1,t;
	for(i=0;i<n;i++)
	{
		cin>>t;
		sum+=t;
		d[sum]++;
		ans = min(ans,n-d[sum]);
		//cout<<d[sum]<<" "<<ans<<endl ;
	}
	cout<<ans<<endl;
	return 0;
}
