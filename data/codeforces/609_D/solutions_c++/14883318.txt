#include <cstdio>
#include <algorithm>

#define rep(i, l, r) for(int i=l; i<=r; i++)
#define down(i, l, r) for(int i=l; i>=r; i--)
#define clr(x, c) memset(x, c, sizeof(x))
#define maxn 200009
#define ll long long

using namespace std;

inline int read()
{
	int x=0, f=1; char ch=getchar();
	while (ch<'0' || ch>'9') {if (ch=='-') f=-1; ch=getchar();}
	while ('0'<=ch && ch<='9') x=x*10+ch-'0', ch=getchar();
	return x*f;
}

struct node{int x,c;} q1[maxn], q2[maxn]; int tot1, tot2;
bool cmp(node a, node b){return a.c<b.c;}
int n, m, k, s, c1[maxn], c2[maxn], c1day[maxn], c2day[maxn]; ll sum1[maxn], sum2[maxn];

bool jub(int x)
{
	rep(i, 0, k) if (i<=tot1 && k-i<=tot2 && sum1[i]*c1[x]+sum2[k-i]*c2[x]<=s) 
		return true;
	return false;
}

int main()
{
	n=read(), m=read(), k=read(), s=read();
	rep(i, 1, n) c1[i]=read();
	rep(i, 1, n) c2[i]=read();
	c1day[1]=1; rep(i, 2, n) if (c1[i-1]>c1[i]) c1day[i]=i; else c1[i]=c1[i-1], c1day[i]=c1day[i-1];
	c2day[1]=1; rep(i, 2, n) if (c2[i-1]>c2[i]) c2day[i]=i; else c2[i]=c2[i-1], c2day[i]=c2day[i-1];
	rep(i, 1, m)
	{
		int t=read(), c=read();
		if (t==1) q1[++tot1]=(node){i,c}; else q2[++tot2]=(node){i,c};
	}
	sort(q1+1, q1+1+tot1, cmp); rep(i, 1, tot1) sum1[i]=sum1[i-1]+q1[i].c;
	sort(q2+1, q2+1+tot2, cmp); rep(i, 1, tot2) sum2[i]=sum2[i-1]+q2[i].c;
	
	
	if (!jub(n)) {puts("-1"); return 0;}
	int l=1, r=n; while (l<r)
	{
		int mid=(l+r)>>1;
		if (jub(mid)) r=mid; else l=mid+1;
	}
	printf("%d\n", l);
	rep(i, 0, k) if (i<=tot1 && k-i<=tot2 && sum1[i]*c1[l]+sum2[k-i]*c2[l]<=s)
	{
		rep(o, 1, i) printf("%d %d\n", q1[o].x, c1day[l]);
		rep(o, 1, k-i) printf("%d %d\n", q2[o].x, c2day[l]);
		return 0;
	}
	return 0;
}