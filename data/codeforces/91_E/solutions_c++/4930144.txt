#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>

using namespace std;

typedef long long LL;
const int MaxN = 101000;
const int Max4N = MaxN * 4;
const int Mdeep = 18 + 1;
struct query{
	int id, L, R, T;
	void read(int _id){
		id = _id;
		scanf("%d%d%d",&L, &R, &T);
	}
} Q[MaxN];

int a[MaxN], b[MaxN], ans[MaxN], Tr[Mdeep][MaxN];
int tz[Max4N], tp[Max4N];
int n, m;
bool cmp(int i, int j) { 
	return (a[i] == a[j])?(b[i] > b[j]):(a[i] > a[j]);
}
bool cmp2(const query &a, const query &b) { 
	return a.T < b.T; 
}
bool cmp3(LL x, LL y, LL t) {
	return a[x] + b[x] * t <= a[y] + b[y] * t;
}

int query(int p, int d, int L, int R, int l, int r, int t) {
	if(l > R || r < L) 
		return -1;
	if(L >= l && R <= r) {
		while (	tz[p]<tp[p] && 
				cmp3(Tr[d][tz[p]], Tr[d][tz[p]+1], t))
			tz[p]++;
		return Tr[d][tz[p]];
	}
	int mid = (L + R) / 2;
	int x = query(p << 1, d + 1, L, mid, l, r, t);
	int y = query(p << 1 | 1, d + 1, mid + 1, R, l, r, t);
	if ((x  < 0) || (y < 0)) 
		return (x < 0)?y:x;
	if (!cmp3(x,y,t))
		return x;
	else
		return y;
}

bool cmps(int i, int j, int k) {
	LL t1 = 1LL * (a[j] - a[k]) * (b[j] - b[i]);
	LL t2 = 1LL * (b[k] - b[j]) * (a[i] - a[j]);
	return t1 <= t2;
}
int id[MaxN];
void build(int p, int d, int L, int R) {
	for(int i = L; i <= R; i++)
		id[i] = i;
	sort(id + L, id + R + 1, cmp);
	tz[p] = L, tp[p] = L - 1;
	for(int i = L; i <= R; i++) {
		if(tz[p]<=tp[p])
			if(b[id[i]] <= b[ Tr[d][tp[p]] ]) 
				continue;
		while ( tz[p] < tp[p] && 
				cmps(Tr[d][tp[p]-1], Tr[d][tp[p]], id[i])) 
			tp[p]--;
		Tr[d][++tp[p]] = id[i];
	}
	if(L >= R) 
		return;
	int mid = (L + R) / 2;
	build(p << 1, d + 1, L, mid);
	build(p << 1 | 1, d + 1, mid+1, R);
}

int main(){
	// freopen("E.in","r",stdin);
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++)
		scanf("%d%d", &a[i], &b[i]);
	for(int i = 0; i < m; i++)
		Q[i].read(i);
	sort(Q, Q + m, cmp2);
	build(1, 0, 0, n-1);
	for(int i = 0; i < m; i++)
		ans[Q[i].id] = query(1, 0, 0, n-1, Q[i].L - 1, Q[i].R - 1, Q[i].T);
	for(int i = 0; i < m; i++)
		printf("%d\n", ans[i]+1);
	return 0;
}