#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
const double eps=1e-8;
const int maxn=100000+10;
struct Point{
	double x,y;
	Point(){}
	Point(double x,double y): x(x),y(y){}
}inter;
struct Line{
	int a,b,c,id;
	Line(){}
	Line(int a,int b,int c,int id): a(a),b(b),c(c),id(id){}
}e[maxn];
struct Node{
	int x,y;
	Node(){}
	Node(int x,int y): x(x),y(y){}
}ans[10];
int n,k,cnt,tot,pos;
inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (ch<'0'||ch>'9')
	{
		if (ch=='-')
			f=-1;
		ch=getchar();
	}
	while (ch>='0'&&ch<='9')
	{
		x=x*10+ch-'0';
		ch=getchar();
	}
	return x*f;
}
inline int dcmp(double x)
{
	if (fabs(x)<eps)
		return 0;
	return x<0 ? -1:1;
}
inline bool judge(int l,int r)
{
	if (dcmp(e[l].a*e[r].b-e[r].a*e[l].b)==0)
		return 0;
	inter=Point(((double)e[l].b*e[r].c-e[l].c*e[r].b)/((double)e[l].a*e[r].b-e[l].b*e[r].a),
				((double)e[l].a*e[r].c-e[l].c*e[r].a)/((double)e[l].b*e[r].a-e[l].a*e[r].b));
	return 1;
}
int main()
{
	n=read(),k=read();
	for (int i=1,a,b,c;i<=n;i++)	
	{
		a=read(),b=read(),c=read();
		e[i]=Line(a,b,c,i);
	}
	cnt=n;
	bool exis=1;
	while (cnt)
	{
		if (k>=cnt)
		{
			ans[++tot]=Node(e[cnt--].id,-1);
			continue;
		}
		for (pos=1;pos<=100;pos++)
		{
			int l=rand()%cnt+1,r=rand()%cnt+1,sz=0;
			if (!judge(l,r))
				continue;
			for (int i=1;i<=cnt;i++)
				if (dcmp((double)e[i].a*inter.x+(double)e[i].b*inter.y+e[i].c)==0)
					sz++;
			if (sz*k>=cnt)
			{
				ans[++tot]=Node(e[l].id,e[r].id);
				break;
			}
		}
		if (pos>100)
		{
			exis=0;
			break;
		}
		for (int i=cnt;i>=1;i--)
			if (dcmp((double)e[i].a*inter.x+(double)e[i].b*inter.y+e[i].c)==0)
				swap(e[i],e[cnt--]);
		k--;
	}
	if (!exis)
		puts("NO");
	else
	{
		puts("YES");
		printf("%d\n",tot);
		for (int i=1;i<=tot;i++)
			printf("%d %d \n",ans[i].x,ans[i].y);
	}
	return 0;
}