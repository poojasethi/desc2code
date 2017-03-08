#include <cstdio>
#include <cstring>
using namespace std;
inline int read() {
	char ch = getchar(); int x = 0;
	while(ch < '0' || ch > '9') ch = getchar();
	while(ch >= '0' && ch <= '9') x = x*10+ch-'0', ch = getchar();
	return x;
}

const int maxn = 1e5+5, size = 26;
int N, M, tot[size];
char s[maxn];

#define mid ((l+r)>>1)
#define lc o<<1, l, mid
#define rc o<<1|1, mid+1, r
struct Segment {
	int tree[maxn<<2], lazy[maxn<<2];
	
	void pushup(int o) { tree[o] = tree[o<<1]+tree[o<<1|1]; }
	void pushdown(int o, int l, int r) {
		if(lazy[o] < 0) return;
		tree[o<<1] = lazy[o]*(mid-l+1);
		tree[o<<1|1] = lazy[o]*(r-mid);
		lazy[o<<1] = lazy[o<<1|1] = lazy[o];
		lazy[o] = -1;
	}
	
	void update(int o, int l, int r, int L, int R, int v) {
		if(L <= l && r <= R) { tree[o] = v*(r-l+1), lazy[o] = v; return; }
		if(r < L || R < l) return;
		pushdown(o, l, r);
		update(lc, L, R, v), update(rc, L, R, v);
		pushup(o);
	}
	
	int query(int o, int l, int r, int L, int R) {
		if(L <= l && r <= R) return tree[o];
		if(r < L || R < l) return 0;
		pushdown(o, l, r);
		int ret = query(lc, L, R)+query(rc, L, R);
		return pushup(o), ret;
	}
} a[size];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	N = read(), M = read();
	scanf("%s", s+1);
	for(int i = 0; i < size; ++i) memset(a[i].lazy, -1, sizeof(a[i].lazy));
	for(int i = 1; i <= N; ++i) a[s[i]-'a'].update(1, 1, N, i, i, 1);
	
	for(int i = 1, l, r; i <= M; ++i) {
		l = read(), r = read();
		int odd = 0, pos = -1;
		for(int j = 0; j < size; ++j) {
			tot[j] = a[j].query(1, 1, N, l, r);
			if(tot[j]&1) ++odd, pos = j, --tot[j];
		}
		if(odd >= 2) continue;
		
		for(int j = 0, h = l, t = r; j < size; ++j) if(tot[j]) {
			int len = tot[j]>>1;
			a[j].update(1, 1, N, l, r, 0);
			a[j].update(1, 1, N, h, h+len-1, 1), a[j].update(1, 1, N, t-len+1, t, 1);
			h += len, t -= len;
		}
		if(pos >= 0) {
			if(!tot[pos]) a[pos].update(1, 1, N, l, r, 0);
			a[pos].update(1, 1, N, mid, mid, 1);
		}
	}
	
	for(int i = 1; i <= N; ++i)
		for(int j = 0; j < size; ++j)
		if(a[j].query(1, 1, N, i, i)) { printf("%c", j+'a'); break; }
	printf("\n");
	return 0;
}			
