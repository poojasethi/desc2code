#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const int oo= 1e9;
int f[40][40][60];
int t,n,m,k;
int dfs(int n,int m,int k){
	int &F= f[n][m][k];	
	if (F!=-1) return F;
	if (!k) return F= 0;
	if (n*m==k) return F= 0;
	F= oo;
	int i,j;
	for (i= 0;i<=k;i++){
		for (j= 1;j<n;j++)
			F= min(F,dfs(j,m,i)+dfs(n-j,m,k-i)+m*m);
		for (j= 1;j<m;j++)
			F= min(F,dfs(n,j,i)+dfs(n,m-j,k-i)+n*n);
	}
	return F;
}
int main()
{
	memset(f,-1,sizeof(f));
	dfs(30,30,50);
	scanf("%d",&t);	
	for (int T= 1;T<=t;T++){
		scanf("%d%d%d",&n, &m, &k);
		if (f[n][m][k]==-1) dfs(n,m,k);
		printf("%d\n",f[n][m][k]);
	}return 0;
}
