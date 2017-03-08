#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int n,x,i,a[100005];
	cin >> n >> x;
	for(i=0;i<n;i++)
		cin >> a[i];
	sort(a,a+n);
	long long int sum=0;
	for(i=0;i<n;i++)
	{
		sum+=a[i]*x;
		if(x>1)
			x--;
	}
	cout << sum;
	return 0;
}