#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#def\
ine F fo\
r
using namespace std;
const int maxn= 20;
int a[maxn][maxn];
int n,i,j,k,M;
int find(int x,int y){
	y>n?x++,y= 1:0;
		M= max(M,a[x][y]);
	return x>n?0:find(x,y+1);
}
int main()
{	
	scanf("%d",&n);
	F(i= 1;i<=n;i++)
		fo\
r(j= 1;j<=n;j++)
			scanf("%d",&a[i][j]);
	F(k= 1;k<=n;k++)
		F(i= 1;i<=n;i++)
		F(j= 1;j<=n;j++)
		a[i][j]= min(a[i][j],a[i][k]+a[k][j]);
	M= 0;
	find(1,1);
	printf("%d",M);
	return 0;
}
