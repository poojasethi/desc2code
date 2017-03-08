#include <cstdio>
#include <algorithm>
struct rec{int x,y,i;};
rec a[1010],ans[1010];
int f[1010],n,m = 0,k,r,tot = 0;
bool v[1010] = {0};
bool cmp(rec a,rec b){
	return a.y > b.y || (a.y == b.y && a.x < b.x);
}
int main(){
	scanf("%d",&n);
	for (int i = 1;i <= n;i++){
		scanf("%d%d",&a[i].x,&a[i].y);
		a[i].i = i;
	}
	std::sort(a + 1,a + n + 1,cmp);
	scanf("%d",&k);
	for (int i = 1;i <= k;i++) scanf("%d",&f[i]);
	for (int i = 1;i <= n;i++){
		r = 0;
		for (int j = 1;j <= k;j++) if (!v[j] && f[j] >= a[i].x){
			if (!r || f[j] < f[r]) r = j;
		}
		if (r){
			m++;
			tot += a[i].y;
			v[r] = 1;
			ans[m].x = a[i].i;
			ans[m].y = r;
		}
	}
	printf("%d %d\n",m,tot);
	for (int i = 1;i <= m;i++) printf("%d %d\n",ans[i].x,ans[i].y);
}
