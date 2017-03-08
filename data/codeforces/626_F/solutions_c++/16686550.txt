#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const int mo= 1e9+7,maxn= 3e3;
int f[210][210][1010];
int a[210];
int n,K,i,j,k,ans;
void update(int &x,int y){
	x= (x+y)%mo;
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d%d",&n, &K);
	for (i= 1;i<=n;i++)
		scanf("%d",&a[i]);
	sort(a+1,a+n+1);
	f[0][0][0]= 1;
	for (i= 1;i<=n;i++)
		for (j= 0;j<=i;j++){
			int y= (a[i]-a[i-1])*j;
			for (k= 0;k+y<=K;k++){
				int &x= f[i-1][j][k];
				update(f[i][j][k+y],x);//单独一组
				update(f[i][j+1][k+y],x);//新开一组
				update(f[i][j][k+y],(ll)x*j%mo);//作为中间元素
				if (j>0)
					update(f[i][j-1][k+y],(ll)x*j%mo);//闭合一组
			}
		}
	for (i= 0;i<=K;i++)
		ans= (ans+f[n][0][i])%mo;
	printf("%d",ans);
}
