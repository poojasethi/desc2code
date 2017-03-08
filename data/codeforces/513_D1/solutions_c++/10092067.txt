#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <ctime>
#define fi first
#define se second
#define PA pair<int,int>
#define VI vector<int>
#define VP vector<PA >
#define mk(x,y) make_pair(x,y)
#define N 1000010
#define For(i,x,y) for (i=x;i<=y;i++)
using namespace std;
struct ww {
	int x,y;
} a[N],b[N];
int i,j,k,n,m,t;
int L[N],R[N],zuo[N],you[N];
VP duan;
inline void fail() {
	printf("IMPOSSIBLE\n");
	exit(0);
}
void print(int x) {
	if (!x) return;
	print(zuo[x]);
	printf("%d ",x);
	print(you[x]);
}
inline bool cc1(const ww &a,const ww &b) {
	return a.x<b.x;
}
inline bool cc2(const ww &a,const ww &b) {
	return a.y>b.y;
}
void dfs(int l,int r) {
	if (l==r) return;
	if (L[l]==0) {
		you[l]=l+1;
		dfs(l+1,r);
		return;
	}
	if (R[l]==N) {
		zuo[l]=l+1;
		dfs(l+1,r);
		return;
	}
	int A=L[l],B=R[l];
	if (A>=B) fail();
	{
		int t=0,i;
		For(i,1,m) if (a[i].x>l&&a[i].y<=r) b[++t]=a[i];
		sort(b+1,b+t+1,cc1);
		int last=0,Zuo=0;
		duan.clear();
		For(i,1,t) {
			if (last<b[i].x) {
				duan.push_back(mk(Zuo,last));
				Zuo=b[i].x,last=b[i].y;
			} else last=max(last,b[i].y);
		}
		duan.push_back(mk(Zuo,last));
		
		int wei=lower_bound(duan.begin(),duan.end(),mk(A+1,0))-duan.begin();
		PA w=duan[wei-1];
		if (w.se>=B) fail();
		int h=max(A,w.se);
		zuo[l]=l+1;
		dfs(l+1,h);
		you[l]=h+1;
		dfs(h+1,r);
	}
}
int main() {
	scanf("%d%d",&n,&m);
	For(i,1,n) L[i]=0,R[i]=N;
	For(i,1,m) {
		int x,y; char p[10];
		scanf("%d%d%s",&x,&y,p);
		if (x>=y) fail();
		a[i]=(ww){x,y};
		if (p[0]=='L') L[x]=max(L[x],y);
		else R[x]=min(R[x],y);
	}
	//sort(a+1,a+m+1,cc1);
	dfs(1,n);
	print(1);
	printf("\n");
	return 0;
}
