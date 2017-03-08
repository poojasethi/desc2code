#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,x[2002],y[2002],ans=0,j,k,area;
	cin >> n;
	for(i=0;i<n;i++)
		cin >> x[i] >> y[i];
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
			for(k=j+1;k<n;k++)
			{
				area=x[i]*(y[j]-y[k])+x[j]*(y[k]-y[i])+x[k]*(y[i]-y[j]);
				if(area)
					ans++;
			}
	cout << ans;
	return 0;
}