// tested from balroginfire
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

const int maxn=400000+10;
int lnk[maxn],nxt[maxn],son[maxn];
vector<int> Free[maxn];
vector< vector<int> > res;
vector<int> root;
bool flag[maxn];
int n,m,now,c1,c2;
vector<int> rv;
pair<int,int> cnt[maxn];
int dnt[maxn];
int masterkill;

void dfs(int u)
{  
    flag[u]=1;
    for (int v=son[u];v;v=nxt[v])
    if (lnk[v]>0)
    {
        lnk[v^1]*=-1;
        if (!flag[lnk[v]])
            dfs(lnk[v]),c2++;
        else
        {
            lnk[v]=lnk[v^1]=0;
            Free[u].push_back(v/2);
            root[root.size()-1]=u;
            c1++;
        }
    }
}

void efs(int u)
{
    dnt[u]=1;
    for (int v=son[u];v;v=nxt[v])
    if (lnk[v]>0)
    {
        efs(lnk[v]);
        dnt[u]+=dnt[lnk[v]];
        if (dnt[lnk[v]]==1) masterkill=u;
    }
}

void go(int u)
{
    for (int v=son[u];v;v=nxt[v])
    if (lnk[v])
    {
        if (lnk[v]<0) lnk[v]*=-1;
        lnk[v^1]=0;

        rv.push_back(lnk[v]);
        go(lnk[v]);
        rv.push_back(u);
        if (now<root.size())
        {
            res.push_back(rv);
            rv.resize(3);
            rv[0]=v/2;rv[1]=u;rv[2]=root[now++];
            res.push_back(rv);
            rv.resize(1);
            rv[0]=root[now-1];
            go(root[now-1]);
            rv.push_back(u);
        }
    }
    for (int i=0;i<Free[u].size();i++)
    if (now<root.size())
    {
        res.push_back(rv);
        rv.resize(3);
        rv[0]=Free[u][i];
        rv[1]=u;rv[2]=root[now++];
        res.push_back(rv);
        rv.resize(1);
        rv[0]=root[now-1];
        go(root[now-1]);
        rv.push_back(u);
    } else break;
}

bool cmp(const int a,const int b)
{return (a==1 || (b!=1 && cnt[a]>cnt[b]));}

int main()
{
    //freopen("input.txt","r",stdin);

    scanf("%d%d",&n,&m);
    for (int i=0,j=1,u,v;i<m;i++)
    {
        scanf("%d%d",&u,&v);
        lnk[++j]=v;nxt[j]=son[u];son[u]=j;
        lnk[++j]=u;nxt[j]=son[v];son[v]=j;
    }

    for (int i=1;i<=n;i++)
    if (!flag[i])
    {
        c1=c2=0;
        root.push_back(i);
        dfs(i);cnt[root[root.size()-1]]=make_pair(c1,c2);
    }

    root[0]=1;
    sort(root.begin(),root.end(),cmp);
    for (int i=1;i<root.size();i++)
    {
        masterkill=root[i];
        efs(root[i]);
        if (!Free[root[i]].size()) root[i]=masterkill;
    }
   
    while (now<root.size())
    {
       
        if (now)
        {
            int k=-1;
            if (Free[root[now]].size())
            {
                k=Free[root[now]][Free[root[now]].size()-1];
                Free[root[now]].pop_back();
            } else
            {
                for (int i=son[root[now]];i;i=nxt[i])
                if (lnk[i]>0 && dnt[lnk[i]]==1)
                {
                    k=i/2;root.push_back(abs(lnk[i]));
                    lnk[i]=lnk[i^1]=0;break;
                }
            }

            if (k==-1) break;
            rv.resize(3);
            rv[0]=k;rv[1]=1;rv[2]=root[now];
            res.push_back(rv);
            rv.clear();
        }
        rv.push_back(root[now++]);
        go(root[now-1]);
        if (rv[rv.size()-1]!=1) rv.push_back(1);
        res.push_back(rv);
    }

    if (now<root.size())
    {
        printf("NO\n");
        return 0;
    }
    printf("YES\n");
    printf("%d\n",res.size()/2);
    for (int i=0;i<res.size();i++)
    if (!(i&1))
    {
        printf("%d",res[i].size());
        for (int j=0;j<res[i].size();j++)
            printf(" %d",res[i][j]);
        printf("\n");
    } else
    printf("%d %d %d\n",res[i][0],res[i][1],res[i][2]);
    }