#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
struct sef{ int ne,en; }h[500050];
int tot,first[500050];
int ans[500050],pre[500050],hei[500050];
int n,m;
char s[500050];
vector < int > V[500050];
inline void setl(int x,int y)
{
    
    h[++tot]=(sef){first[x],y};
    first[x]=tot;
    return;
}
inline void dfs(int x,int d)
{
    int g=V[x].size(),id;
    for (int i=0;i<g;++i)
    {
        id=V[x][i];
        ans[id]^=pre[hei[id]];
    }
    for (int i=first[x];i;i=h[i].ne)
    {
        dfs(h[i].en,d+1);
    }
    pre[d]^=1<<s[x]-'a';
    for (int i=0;i<g;++i)
    {
        id=V[x][i];
        ans[id]^=pre[hei[id]];
    }
}
int main()
{
    scanf("%d%d",&n,&m);
    int x,y;
    for (int i=2;i<=n;++i)
    {
        scanf("%d",&x);
        setl(x,i);
    }
    scanf("%s",s+1);
    for (int i=1;i<=m;++i)
    {
        scanf("%d%d",&x,hei+i);
        V[x].push_back(i);
    }
    dfs(1,1);
    for (int i=1;i<=m;++i)
    {
        if (ans[i]&(ans[i]-1)) printf("No\n");
        else printf("Yes\n");
    }
}