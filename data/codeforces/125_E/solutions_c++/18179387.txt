#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
#define M 100010
#define N 5010

struct Edge {
    int id, u, v;
    double w;
    bool operator <(const Edge &e)const {
        return w < e.w;
    }
};

int cnt;
int n,m,k;
Edge e[M];
Edge e1[M];
int f[N];
int ans[M];
double mid;
int top;

int find(int x)
{
    if(x != f[x]) f[x] = find(f[x]);
    return f[x];
}
int kruskal()
{
    top = cnt = 0;
    for(int i = 0; i < m; i++) {
        e1[i] = e[i];
        e1[i].w += e1[i].u == 1 ? mid : 0;
    }
    for(int i = 1; i <= n; i++) f[i] = i;
    sort(e1, e1 + m);
    for (int i = 0; i < m; i++) {
        int u = find(e1[i].u);
        int v = find(e1[i].v);
        if(u != v) {
            ans[top++] = e1[i].id;
            cnt += e1[i].u == 1;
            f[u] = v;
        }
    }
    return cnt;
}
int main()
{
    scanf("%d%d%d",&n, &m, &k);
    for (int i = 0; i < m; i++) {
        scanf("%d%d%lf", &e[i].u, &e[i].v, &e[i].w);
        if(e[i].u > e[i].v) swap(e[i].u, e[i].v);
        e[i].id = i + 1;
    }

    double l=-1e5, r=1e5;
    while(l < r) {
        mid = (l + r) / 2;
        cnt = kruskal();
        if(cnt == k) break;
        if(cnt < k) r = mid;
        else l = mid;
    }
    if (cnt == k) {
        printf("%d\n",n-1);
        for (int i = 0; i < top; i++)
            printf("%d ",ans[i]);
    }
    else {
        printf("-1\n");
    }
    return 0;
}