#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
const int maxn= 3e3;
struct people{
	int t,s,f,v,m;
}a[maxn],I,J;
int r[maxn];
int n,i,j;
int main()
{
	scanf("%d",&n);
	for (i= 1;i<=n;i++){
		scanf("%d%d%d",&a[i].t, &a[i].s, &a[i].f);
		a[i].m= abs(a[i].f-a[i].s);
		a[i].v= (a[i].f-a[i].s)/a[i].m;
	}
	for (i= 1;i<=n;i++){
		for (j= i+1;j<=n;j++){
			I= a[i];
			J= a[j];
			if (a[i].t>a[j].t) swap(I,J);
			if (I.t+I.m<J.t) continue;
			int m= min(I.t+I.m-J.t,J.m);
			int bi= I.s+(J.t-I.t)*I.v;
			if (I.v==J.v){
				if (bi==J.s) r[i]++,r[j]++;
				continue;
			}
			int ei= bi+m*I.v;
			int bj= J.s;
			int ej= J.s+m*J.v;
			if (bi>ei) swap(bi,ei);
			if (bj>ej) swap(bj,ej);
			if (bi>bj){
				swap(bi,bj);
				swap(ei,ej);
			}
			if (bj<=ei) r[i]++,r[j]++;
		}
	}
	for (i= 1;i<=n;i++)
		printf("%d%c",r[i],i<n?' ':'\n');
	return 0;
}
