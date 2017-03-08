#include <cstdio>
#include <algorithm>
#define UPD(x, y) \
	if (x < y) \
x = y;

using namespace std;
const int N_MAX = 1000010;
struct Node {
	int cnt[2], res[2], l, r, sz, tag;
} node[N_MAX * 4];
char arr[N_MAX];

void update(int i) {
	Node &x = node[i],
		 &lch = node[i * 2],
		 &rch = node[i * 2 + 1];
	for (int t = 0; t < 2; t ++)
		x.cnt[t] = lch.cnt[t] + rch.cnt[t];
	x.res[0] = lch.cnt[0] + rch.cnt[1];
	UPD(x.res[0], lch.res[0] + rch.cnt[1]);
	UPD(x.res[0], lch.cnt[0] + rch.res[0]);
	x.res[1] = lch.cnt[1] + rch.cnt[0];
	UPD(x.res[1], lch.res[1] + rch.cnt[0]);
	UPD(x.res[1], lch.cnt[1] + rch.res[1]);
}

void mark(int i) {
	Node &x = node[i];
	x.tag ^= 1;
	swap(x.res[0], x.res[1]);
	swap(x.cnt[0], x.cnt[1]);
}

void push_down(int i) {
	if (node[i].tag) {
		mark(i * 2), mark(i * 2 + 1);
		node[i].tag = 0;
	}
}

void build(int i, int l, int r) {
	node[i].l = l, node[i].r = r, node[i].sz = r - l + 1;
	if (l == r) {
		Node &x = node[i];
		int t = arr[l] == '7';
		x.cnt[t] = 1;
		x.res[0] = x.res[1] = 1;
		return;
	}
	int mid = (l + r) / 2;
	build(i * 2, l, mid);
	build(i * 2 + 1, mid + 1, r);
	update(i);
}

void change(int i, int l, int r) {
	if (node[i].l > r || node[i].r < l)
		return;
	if (l <= node[i].l && node[i].r <= r) {
		mark(i);
		return;
	}
	push_down(i);
	change(i * 2, l, r);
	change(i * 2 + 1, l, r);
	update(i);
}

int main() {
//	freopen("t.in", "r", stdin);
	int n, m;
	scanf("%d%d", &n, &m);
	scanf("%s", arr + 1);
	build(1, 1, n);
	while (m --) {
		static char cmd[11];
		scanf("%s", cmd);
		if (cmd[0] == 'c')
			printf("%d\n", node[1].res[0]);
		else {
			int l, r;
			scanf("%d%d", &l ,&r);
			change(1, l, r);
		}
	}
}
