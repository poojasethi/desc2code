#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int a[2222][2222], b[2222][2222];
int vis[2222];

int main() {
    int n;
    cin >> n;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
        scanf("%d", &a[i][j]);
        b[i][j] = 1e9+7;
    }
    for(int i=0;i<n;i++) b[i][i] = 0;
    priority_queue <pair<int,pii> > q;
    q.push(mp(0,mp(0,-1)));
    int ed = 0;
    while(!q.empty()) {
        int u = q.top().ss.ff;
        int p = q.top().ss.ss;
        int s = -q.top().ff;
        q.pop();
        if(vis[u]) continue;
        b[u][p] = b[p][u] = s;
        vis[u] = 1;
        ed++;
        for(int i=0;i<n;i++) if(vis[i]) b[i][u] = b[u][i] = min(b[i][u],b[i][p]+b[p][u]);
        for(int i=0;i<n;i++) {
            if(a[u][i] != 0 && !vis[i]) q.push(mp(-a[u][i],mp(i,u))); 
        }
    }
    int ok = 1;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(a[i][j] != b[i][j]) ok = 0;
    cout << (ok ? "YES" : "NO") << endl;
    return 0;
}

