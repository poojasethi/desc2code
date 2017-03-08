#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,a[103];
	cin >> n;
	for(int i=0;i<n;i++)
		cin >> a[i];
	sort(a+1,a+n);
	int cnt=0;
	while(a[0]<=a[n-1])
	{
		a[0]++;
		a[n-1]--;
		sort(a+1,a+n);
		cnt++;
	}
	cout << cnt;
	return 0;
}