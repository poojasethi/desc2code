#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;
const int dx[5]={0,-1,0,1,0},dy[5]={0,0,1,0,-1};
int ans[101];
bool vst[101][101],mp[101][101][4];
queue<pair<int,int> > q;
int main()
{
	int n,m,k,i,x1,y1,x2,y2,j,ord=0,siz,l;
	scanf("%d%d%d",&n,&m,&k);
	for (i=1;i<=k;i++)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		if (x1==x2)
			for (j=y1+1;j<=y2;j++)
			{
				mp[x1][j][2]=true;
				mp[x1+1][j][0]=true;
			}
		else
			for (j=x1+1;j<=x2;j++)
			{
				mp[j][y1][1]=true;
				mp[j][y1+1][3]=true;
			}
	}
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
			if (!vst[i][j])
			{
				q.push(make_pair(i,j));
				vst[i][j]=true;
				siz=0;
				ord++;
				while (!q.empty())
				{
					pair<int,int> f=q.front();
					q.pop();
					siz++;
					for (l=1;l<=4;l++)
					{
						if (!mp[f.first][f.second][l-1])
						{
							int ox=f.first+dx[l],oy=f.second+dy[l];
							if (ox>0&&ox<=n&&oy>0&&oy<=m&&!vst[ox][oy])
							{
								vst[ox][oy]=true;
								q.push(make_pair(ox,oy));
							}
						}
					}
				}
				ans[ord]=siz;
			}
	sort(ans+1,ans+ord+1);
	for (i=1;i<=ord;i++)
		printf("%d ",ans[i]);
	return 0;
}
