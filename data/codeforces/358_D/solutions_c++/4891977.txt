#include<iostream>
using namespace std;
int n,a[3010],b[3010],c[3010];
int best[2][3010];

int main()
{
	int i;
	cin>>n;
	for(i=1;i<=n;i++)
		cin>>a[i];
	for(i=1;i<=n;i++)
		cin>>b[i];
	for(i=1;i<=n;i++)
		cin>>c[i];
	
	best[0][1]=b[1];
	best[1][1]=a[1];
	for(i=2;i<=n;i++)
	{
		best[0][i]=max(best[0][i-1]+b[i],best[1][i-1]+c[i]);
		best[1][i]=max(best[0][i-1]+a[i],best[1][i-1]+b[i]);
	}
	cout<<best[1][n]<<"\n";
	return 0;
}
