#include <bits/stdc++.h>
using namespace std;
int a[100010];
long long sum=0;
int main()
{
	int n;
	cin>>n;
	int cnt=0;
	for(int i=0;i<n;i++) cin>>a[i];
	sort(a,a+n);
	for(int i=0;i<=n;i++)
	{
		if(a[i]>=sum) {cnt++;
		sum+=a[i];}
	}
	cout<<cnt;
	return 0;
}
