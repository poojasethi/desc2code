#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
const int maxn= 300;
struct dish{
	int a,b;
	bool operator <(const dish &c)const{
		return a<c.a;
	}
}d[maxn];
int m[maxn],b[maxn];
int i,n,x,y,M,l,r,max_t;
bool ok(int mid){
	int i,j,k,p;
	for (i= 1;i<=n;i++){
		m[i]= mid;
		b[i]= 1;
	}
	j= 1;
	for (i= 0;i<=max_t;i++){
		while (j<=n && d[j].a==i) j++;
		p= 0;
		for (k= 1;k<j;k++)
			if (m[k]&&d[k].a<=i&&d[k].b>i){
				if (!p || d[p].b-i-m[p]>d[k].b-i-m[k])
					p= k;
			}
		if (p)
			m[p]--;
	}
	for (i= 1;i<=n;i++)
		if (m[i]) return 0;
	return 1;
}
int main()
{
	scanf("%d",&n);
	for (i= 1;i<=n;i++){
		scanf("%d%d",&x, &y);
		d[i]= (dish){x,y};
		M= max(M,y-x);
		max_t= max(max_t,y);
	}
	sort(d+1,d+n+1);
	l= 0;r= M+1;
	while (l+1<r){
		int mid= (l+r)>>1;
		if (ok(mid)) l= mid;
		else r= mid;
	}
	printf("%d",n*l);
	return 0;
}
