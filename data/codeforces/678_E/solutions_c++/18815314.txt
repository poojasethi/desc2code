#include<bits/stdc++.h>
using namespace std;

const int maxn = 18;
double d[1<<maxn][maxn];
double p[maxn][maxn];
int n;

double cal(int msk,int i)
{
	double& ans = d[msk][i];
	if(ans > -1) return ans;
	if(msk == (1<<n)-1) return ans = !i;
	for(int j=0;j<n;++j) if(!((1<<j)&msk))
	{
		double cur = cal(msk|(1<<j),i)*p[i][j];
		cur += cal(msk|(1<<j),j)*p[j][i];
		ans = max(ans,cur);
	}
	return ans;
}

int main()
{
	//freopen("test.txt","r",stdin);
	cin >> n;
	for(int i=0;i<n;++i)
		for(int j=0;j<n;++j)
			cin >> p[i][j];

	if(n == 1)
	{
		printf("%.9lf\n",1.0);
		return 0;
	}
	for(int i=0;i<(1<<n);++i)
		for(int j=0;j<n;++j) d[i][j] = -1;


	double ans = 0;
	for(int i=0;i<n;++i)
		for(int j=0;j<i;++j)
		{
			int msk = (1<<i) | (1<<j);
			double cur = cal(msk,i)*p[i][j];
			cur += cal(msk,j)*p[j][i];
			ans = max(ans,cur);
		}
	printf("%.9lf\n",ans);
	return 0;
}

