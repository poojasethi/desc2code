#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,m,a[103],i;
	cin >> n >> m;
	for(int i=0;i<n;i++)
		cin >> a[i];
	sort(a,a+n);
	i=n-1;
	int cnt=0;
	while(m>0)
	{
		m=m-a[i--];
		cnt++;
	}
	cout << cnt;
	return 0;
}