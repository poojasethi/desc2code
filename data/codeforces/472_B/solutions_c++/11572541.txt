#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,k,pos,ans,i,a[2004];
	cin >> n >> k;
	for(i=0;i<n;i++)
		cin >> a[i];
	sort(a,a+n);
	pos=n-1;
	ans=0;
	while(pos>=0)
	{
		ans+=2*(a[pos]-1);
		pos-=k;
	}
	cout << ans;
	return 0;
}