#include <iostream>
#define isformed(i,j) mp[i][j]&&mp[i+1][j]&&mp[i][j+1]&&mp[i+1][j+1]
using namespace std;
bool mp[1005][1005];
int x[100001],y[100001];
int main()
{
	int n,m,k,i,t=0;
	bool f=false;
	cin>>n>>m>>k;
	for (i=1;i<=k;i++)
	{
		cin>>x[i]>>y[i];
		mp[x[i]][y[i]]=true;
		if ((isformed(x[i]-1,y[i]-1)||isformed(x[i]-1,y[i])||isformed(x[i],y[i]-1)||isformed(x[i],y[i]))&&!f)
		{
			f=true;
			t=i;
		}
	}
	cout<<t;
	return 0;
}
