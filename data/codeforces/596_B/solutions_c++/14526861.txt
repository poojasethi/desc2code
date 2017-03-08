#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int ans=0,n,a[200000],i;
	cin>>n;
	for(i=0;i<n;i++)
	cin>>a[i];
	ans = abs(a[0]);
	for(i=1;i<n;i++)
	ans+= abs(a[i] - a[i-1]);
	cout<<ans<<endl;
	return 0;
}
