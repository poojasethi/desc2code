#include <cstdio>
#define N 1005
double f[N][N];
int main()
{
	int n,m; scanf("%d%d",&n,&m);
	for(int i=0;i<=m;i++) f[0][i]=0;
	for(int i=1;i<=n;i++) f[i][0]=1;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
		{
			double a=i,b=j;
			if(j>=3)
				f[i][j]=a/(a+b)+b/(a+b)*((b-1)/(a+b-1))*(a/(a+b-2)*f[i-1][j-2]+(b-2)/(a+b-2)*f[i][j-3]);
			else if(j==2) 
				f[i][j]=a/(a+b)+b/(a+b)*((b-1)/(a+b-1))*f[i-1][j-2];
			else f[i][j]=a/(a+b);
		}
	printf("%.9lf",f[n][m]);
}