#include<bits/stdc++.h>
using namespace std;
int g[305][305],s[305][305];
int n,m;
int bfs(int src,int sink) {
    queue<int> q;
    q.push(src);
    int from[305];
    bool visited[305];
    for(int i=0;i<305;i++) {
        from[i]=-1;
        visited[i]=false;
    }
    bool flag=true;
    visited[src]=true;
    while(!q.empty()) {
        int v=q.front();
        q.pop();
        for(int i=1;i<=n;i++) {
            if(g[v][i]>0 && !visited[i]) {
                q.push(i);
                from[i]=v;
                visited[i]=true;
                if(i==sink) { flag=false; break;}
            }
        }
        if(!flag) break;
    }
    int v=sink;
    int path_cap=INT_MAX;
    while(from[v]!=-1) {
        int t=from[v];
        path_cap=min(path_cap,g[t][v]);
        v=t;
    }
    v=sink;
    while(from[v]!=-1) {
        int t=from[v];
        g[t][v]-=path_cap;
        g[v][t]+=path_cap;
        v=t;
    }
    //cout<<path_cap<<endl;
    return path_cap;
}
int flow(int src,int sink) {
    int ans=0;
    while(true) {
        int got=bfs(src,sink);
        if(got==INT_MAX) break;
        else ans+=got;
    }
    return ans;
}
int main()
{
    int a,w,b;
    scanf("%d%d",&n,&m);
    for(int i=0;i<m;i++) {
        scanf("%d%d%d",&a,&b,&w);
        g[a][b]=w;
        s[a][b]=w;
    }
    int t,src,sink;
    scanf("%d",&t);
    while(t--) {
        for(int i=1;i<=n;i++) {
            for(int j=1;j<=n;j++) g[i][j]=s[i][j];
        }
        scanf("%d%d",&src,&sink);
        printf("%d\n",flow(src,sink));
    }
    return 0;
}
