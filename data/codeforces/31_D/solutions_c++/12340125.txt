#include <stdio.h>
#include <algorithm>
using namespace std;
struct part
{
	int x,y,w,h;
	part(){}
	part(int _x,int _y,int _w,int _h){x=_x;y=_y;w=_w;h=_h;}
};
struct cut
{
	int x1,y1,x2,y2;
};
bool inrange(int x1,int y1,int x2,int y2,part p)
{
	if (x1==x2)
		return x1>=p.x&&x1<=p.x+p.h&&y1==p.y&&y2==p.y+p.w;
	else
		return y1>=p.y&&y1<=p.y+p.w&&x1==p.x&&x2==p.x+p.h;
}
part p[101];
int ans[101];
cut c[101];
bool used[101];
int main()
{
	int w,h,n,i,j,k,cnt=1;
	scanf("%d%d%d",&h,&w,&n);
	p[1]=part(0,0,w,h);
	for (i=1;i<=n;i++)
		scanf("%d%d%d%d",&c[i].x1,&c[i].y1,&c[i].x2,&c[i].y2);
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
			for (k=1;k<=cnt;k++)
				if (!used[j]&&inrange(c[j].x1,c[j].y1,c[j].x2,c[j].y2,p[k]))
				{
					if (c[j].x1==c[j].x2)
					{
						p[++cnt]=part(c[j].x1,p[k].y,p[k].w,p[k].x+p[k].h-c[j].x1);
						p[k].h=c[j].x1-p[k].x;
					}
					else
					{
						p[++cnt]=part(p[k].x,c[j].y1,p[k].y+p[k].w-c[j].y1,p[k].h);
						p[k].w=c[j].y1-p[k].y;
					}
					used[j]=true;
					break;
				}
	for (i=1;i<=n+1;i++)
		ans[i]=p[i].w*p[i].h;
	sort(ans+1,ans+n+1+1);
	for (i=1;i<=n+1;i++)
		printf("%d ",ans[i]);
	return 0;
}
