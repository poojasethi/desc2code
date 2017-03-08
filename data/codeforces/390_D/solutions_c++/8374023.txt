#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;
int n,m,k,sb,ci,ans,done,st,ed,x,y;
string s[51][51];
int inq[51][51];
struct ORZ
{
	int x,y;
	string s;
}h[10000];
inline bool cmp(ORZ x,ORZ y){return x.x+x.y>y.x+y.y;}
int main()
{
	scanf("%d%d%d",&n,&m,&k);
	char t[50];
	sprintf(t,"(%d,%d)",1,1);
	h[1]=(ORZ){1,1,t};inq[1][1]++;
	done=1;
	for(st=ed=1;st<=ed;st++)
	{
		
		x=h[st].x;y=h[st].y;
		if(x==1&&y<m)
		{
			h[++ed].x=1;h[ed].y=y+1;inq[x][y+1]++;
			char t[50];sprintf(t," (%d,%d)",1,y+1);h[ed].s=h[st].s+t;
			done++;if(done==k)break;
		}
		if(x<n)
		{
			h[++ed].x=x+1;h[ed].y=y;inq[x+1][y]++;
			char t[50];sprintf(t," (%d,%d)",x+1,y);h[ed].s=h[st].s+t;
			done++;if(done==k)break;
		}
	}
	sort(h+1,h+k+1,cmp);
	ans=0;
	for(int i=1;i<=k;i++)ans+=h[i].x+h[i].y-1;
	printf("%d\n",ans);
	for(int i=1;i<=k;i++)puts(&h[i].s[0]);
}