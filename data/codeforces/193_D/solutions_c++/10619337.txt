#include <iostream>
#include <cstdio>
using namespace std;
#define lson x<<1
#define rson x<< 1 | 1
const int MAXN = 300009;
struct Segtree {
    int l, r, val, add, tol, tol2;
} St[MAXN << 2];
int p[MAXN], a[MAXN];
int n;
long long ans;
void Build (int x, int l, int r) {
    St[x].l = l, St[x].r = r;
    St[x].tol = r - l + 1;
    if (l == r) return;
    int mid = (l + r) >> 1;
    Build (lson, l, mid), Build (rson, mid + 1, r);
}
void push (int x) {
    if (St[x].add == 0) return;
    St[lson].add +=St[x].add, St[rson].add += St[x].add;
    St[lson].val += St[x].add, St[rson].val += St[x].add;
    St[x].add = 0;
}
void update (int x) {
    St[x].val = min (St[lson].val, St[rson].val);
    St[x].tol = St[lson].tol * (St[x].val == St[lson].val) + St[rson].tol * (St[x].val == St[rson].val);
    St[x].tol2=St[lson].tol*(St[x].val+1==St[lson].val)+St[rson].tol*(St[x].val+1==St[rson].val);
    St[x].tol2+=St[lson].tol2*(St[x].val==St[lson].val)+St[rson].tol2*(St[x].val==St[rson].val);
}
void Modify (int x, int l, int r, int key) {
    if (St[x].l >= l && St[x].r <= r) {
        St[x].val += key, St[x].add += key;
        return;
    }
    push (x);
    int mid = (St[x].l + St[x].r) >> 1;
    if (mid >= l) Modify (lson, l, r, key);
    if (mid < r) Modify (rson, l, r, key);
    update (x);
}
void Query (int x, int l, int r) {
    if (St[x].l >= l && St[x].r <= r) {
        ans += St[x].tol * (St[x].val <=2)+St[x].tol2*(St[x].val==1);
        return;
    }
    push (x);
    int mid = (St[x].l + St[x].r) >> 1;
    if (mid >= l) Query (lson, l, r);
    if (mid < r) Query (rson, l, r);
}
int main() {
    scanf ("%d", &n);
    for (int i = 1, x; i <= n; i++) {
        scanf ("%d", &x);
        p[x] = i;
    }
    Build (1, 1, n);
    for (int i = n; i; i--) {
        a[p[i]] = i;
        int x = a[p[i] - 1], y = a[p[i] + 1];
        if (x > y) swap (x, y);
        if (x) Modify (1, i, x - 1, 1), Modify (1, y, n, -1);
        else if (y) Modify (1, i, y - 1, 1);
        else Modify (1, i, n, 1);
        Query (1, i, n);
    }
    printf ("%I64d", ans-n);
}