#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
int n,m,k,x,y,a,b,d[2010][2010],v[2010][2010];
bool solve(int x,int y,int k) {
	int l=max(1,x-k),r=min(x+k,n),t;
	rep(i,l,r+1) {
		t=k-abs(i-x);
		if (y-t>0&&!v[i][y-t]) return a=i,b=y-t,1;
		if (y+t<=m&&!v[i][y+t]) return a=i,b=y+t,1;
	}
	return 0;
}
int main() {
	scanf("%d%d%d",&n,&m,&k);
	rep(t,0,k) {
		scanf("%d%d",&x,&y);
		rep(i,-2,3) rep(j,-2,3) {
			if (x+i<1||x+i>n||y+j<1||y+j>m) continue;
			d[x][y]=max(d[x][y],d[x+i][y+j]-abs(i)-abs(j));
		}
		while (!solve(x,y,d[x][y])) d[x][y]++;
		printf("%d %d\n",a,b);
		v[a][b]=1;
	}
}
