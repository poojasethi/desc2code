#include <stdio.h>
char a[251][251];
int n,m,cnt,ans;
const int dx[9]={0,0,1,0,-1,1,1,-1,-1},dy[9]={0,1,0,-1,0,1,-1,1,-1};
void dfs(int x,int y)
{
	int i;
	a[x][y]='2';
	cnt++;
	for (i=1;i<=8;i++)
	{
		int ox=x+dx[i],oy=y+dy[i];
		if (ox>0&&ox<=n&&oy>0&&oy<=m&&a[ox][oy]=='1')
			dfs(x+dx[i],y+dy[i]);
	}
}
bool check(int x,int y,int d,int left,int right)
{
	int i,j;
	for (i=0;i<=d;i++)
		for (j=left;j<right;j++)
			if (x+dx[j]*i<=0||x+dx[j]*i>n||y+dy[j]*i<=0||y+dy[j]*i>m||a[x+dx[j]*i][y+dy[j]*i]!='2')
				return false;
	return true;
}
int main()
{
	int q,i,j;
	scanf("%d",&q);
	while (q--)
	{
		ans=0;
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++)
			scanf("%s",a[i]+1);
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				if (a[i][j]=='1')
				{
					cnt=0;
					dfs(i,j);
					int r=cnt;
					if (r%4==0&&r/4<=250)
					{
						ans+=check(i,j,r/4,1,3)&&check(i+r/4,j+r/4,r/4,3,5);
						ans+=check(i,j,r/4,5,7)&&check(i+r/2,j,r/4,7,9);
					}
				}
		printf("%d\n",ans);
	}
	return 0;
}
