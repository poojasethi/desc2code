#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int n,a[100002],s=0,cnt=0,rem;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		cin >> a[i];
		s+=a[i];
	}
	rem=s%n;
	s=s/n;
	sort(a,a+n);
	for(int i=n-1;i>=0;i--)
	{
		if(a[i]>s && rem>0)
		{
			cnt+=a[i]-s-1;
			rem--;
		}
		else if(a[i]>s && rem==0)
		{
			cnt+=a[i]-s;
		}
	}
	cout << cnt;
	return 0;
}