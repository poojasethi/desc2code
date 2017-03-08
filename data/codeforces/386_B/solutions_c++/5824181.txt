#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int n,t;
	int a[1000];
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	cin>>t;
	sort(a,a+n);
	int c = 0;
	int mx = -99999;
	for(int i=0;i<n;i++)
	{
		c = 1;
		for(int j=i+1;j<n;j++)
		{
			if(a[j]-a[i]<=t)
			{
				c++;
			}
		}
		mx = max(mx,c);
	}
	cout<<mx;
	return 0;
}