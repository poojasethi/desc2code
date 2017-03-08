#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define D 42
using namespace std;

int xa,xb,xc,da,db,dc,ta,tb,tc,ans;
bool f[D+5][D+5][D+5][8][8][8];

void calc(int a,int b,int c,int aa,int bb,int cc)
{
	if (a<0||b<0||c<0) return;
	if (a==b||a==c||b==c||f[a][b][c][aa][bb][cc]) return;
	int x=max(a>D?0:a,max(b>D?0:b,c>D?0:c)),y=min(a,min(b,c));
	ans=max(ans,x),f[a][b][c][aa][bb][cc]=1;
	if (a<=D)
	{
		if (aa==1||aa==7) for (int i=a+da; i>=a-da&&i>=y-1; i--) calc(i,b,c,aa^1,bb,cc);
		if (aa&2)
		{
			if (b==a-1||b==a+1) calc(a,D+1,c,aa^2,bb,cc);
			if (c==a-1||c==a+1) calc(a,b,D+1,aa^2,bb,cc);
		}
		if ((aa&4)&&!(aa&2)) for (int i=a+ta; i>=a-ta&&i>=y-1; i--)
		{
			if (b==D+1) calc(a,i,c,aa^4,bb,cc);
			if (c==D+1) calc(a,b,i,aa^4,bb,cc);
		}
	}
	if (b<=D)
	{
		if (bb==1||bb==7) for (int i=b+db; i>=b-db&&i>=y-1; i--) calc(a,i,c,aa,bb^1,cc);
		if (bb&2)
		{
			if (a==b-1||a==b+1) calc(D+2,b,c,aa,bb^2,cc);
			if (c==b-1||c==b+1) calc(a,b,D+2,aa,bb^2,cc);
		}
		if ((bb&4)&&!(bb&2)) for (int i=b+tb; i>=b-tb&&i>=y-1; i--)
		{
			if (a==D+2) calc(i,b,c,aa,bb^4,cc);
			if (c==D+2) calc(a,b,i,aa,bb^4,cc);
		}
	}
	if (c<=D)
	{
		if (cc==1||cc==7) for (int i=c+dc; i>=c-dc&&i>=y-1; i--) calc(a,b,i,aa,bb,cc^1);
		if (cc&2)
		{
			if (a==c-1||a==c+1) calc(D+3,b,c,aa,bb,cc^2);
			if (b==c-1||b==c+1) calc(a,D+3,c,aa,bb,cc^2);
		}
		if ((cc&4)&&!(cc&2)) for (int i=c+tc; i>=c-tc&&i>=y-1; i--)
		{
			if (a==D+3) calc(i,b,c,aa,bb,cc^4);
			if (b==D+3) calc(a,i,c,aa,bb,cc^4);
		}
	}
}

void doit()
{
	scanf("%d%d%d%d%d%d%d%d%d",&xa,&da,&ta,&xb,&db,&tb,&xc,&dc,&tc);
	calc(xa,xb,xc,7,7,7),printf("%d\n",ans);
}

int main()
{
	doit();
	return 0;
}