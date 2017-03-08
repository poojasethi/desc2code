#include<cstdio>
#include<algorithm>
#define lowbit(x) x&(-x)
using namespace std;
struct kk{int x,y,id;}a[200010];
int i,n,c[200010],ans[200010];
bool cmp(kk i,kk j)  {return i.x<j.x;}
bool cmp1(kk i,kk j){return i.y<j.y;}
void modify(int s)
{
	for (;s<=200010;s+=lowbit(s))
	   c[s]++;
}
int sum(int s)
{
	int ans=0;
	for (int i=s;i;i-=lowbit(i))
	   ans+=c[i];
	return ans;
}
int main()
{
	scanf("%d",&n);
	for (i=1;i<=n;i++) {scanf("%d%d",&a[i].x,&a[i].y);a[i].id=i;}
	sort(a+1,a+n+1,cmp1);
	for (i=1;i<=n;i++) a[i].y=i;
	sort(a+1,a+n+1,cmp);
	for (i=n;i>=1;i--)
	{
		ans[a[i].id]=sum(a[i].y);
	    modify(a[i].y);
    }
    for (i=1;i<=n;i++) printf("%d\n",ans[i]);
    return 0;
}