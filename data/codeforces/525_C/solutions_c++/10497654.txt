#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int n,a[100005],i,x;
	cin >> n;
	for(i=0;i<n;i++)
		cin >> a[i];
	sort(a,a+n);
	long long int ans=0;
	int count=0;
	for(i=n-1;i>0;i--)
	{
		if(a[i]==a[i-1] || a[i]==a[i-1]+1)
		{
			if(count==0)
			{
				x=a[i-1];
				count=1;
			}
			else if(count==1)
			{
				ans+=a[i-1]*x;
				count=0;
			}
			i--;
		}
	}
	cout << ans;
	return 0;
}