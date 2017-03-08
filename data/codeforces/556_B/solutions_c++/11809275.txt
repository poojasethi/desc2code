#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,a[1005];
	cin >> n;
	for(i=0;i<n;i++)
	{
		cin >> a[i];
		if(i%2==0)
			a[i]=(i-a[i]+n)%n;
		else
			a[i]=(a[i]-i+n)%n;
	}
	for(i=0;i<n;i++)
	{
		if(a[i]!=a[0])
		{
			cout << "No";
			return 0;
		}
	}
	cout << "Yes";
	return 0;
}