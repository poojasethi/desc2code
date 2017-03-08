#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,a[1002];
	cin >> n;
	for(int i=0;i<n;i++)
		cin >> a[i];
	int cnt=0,ans=0,i=0,p=1;
	while(cnt<n)
	{
		if(a[i]<=cnt)
		{
			cnt++;
			a[i]=n+3;
		}
		if(cnt==n)
			break;
		i+=p;
		if(i==n)
		{
			ans++;
			p=-1;
			i=n-1;
		}
		else if(i==-1)
		{
			ans++;
			p=1;
			i=0;
		}
	}
	cout << ans;
	return 0;
}