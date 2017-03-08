#include<bits/stdc++.h>
using namespace std;
int main()
{
	int i,n,d,m,cost = 0;
	int a[100];
	cin>>n>>d;
	for(i=0;i<n;i++)
	cin>>a[i];
	sort(a,a+n);
	cin>>m;
	for(i=0;i<min(m,n);i++)
	cost += a[i];
	m = m - n;
	if (m > 0)
	cost-= d * m;
	cout<<cost<<endl;
	return 0;
}
