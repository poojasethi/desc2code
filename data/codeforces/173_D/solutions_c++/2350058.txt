#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int mn=101000;
struct list
{
    int tt,la[mn],next[mn*2],y[mn*2];
    void add(int i,int j){next[++tt]=la[i],la[i]=tt,y[tt]=j;}
}e;
int c[mn],ans[mn];
int d[mn];
int n,m,i,j,k,x,y,s1,s2,t,s;
bool u[mn];
void dfs(int r,int v)
{
    c[r]=v;
    if(v==1)++s1;else ++s2;
    for(int p=e.la[r];p;p=e.next[p])if(!c[e.y[p]])dfs(e.y[p],3-v);
}
void rev()
{
    int i;
    swap(s1,s2);
    fo(i,1,n)c[i]=3-c[i];
}
bool solve()
{
    int i,k,p,j;
    k=0;
    fo(i,1,n)
        if(c[i]==1&&!ans[i]&&d[i]<d[k])k=i;
    if(d[k]>s2-2)return 0;
    ans[k]=++s;
    memset(u,0,sizeof u);
    for(p=e.la[k];p;p=e.next[p])u[e.y[p]]=1;
    j=0;
    fo(i,1,n)
        if(c[i]==2&&!ans[i]&&!u[i])
        {
            ans[i]=++s,++j;
            if(j==2)break;
        }
    return 1;
}
int main()
{
    scanf("%d%d",&n,&m);
    fo(i,1,m)
    {
        scanf("%d%d",&x,&y);
        ++d[x],++d[y];
        e.add(x,y),e.add(y,x);
    }
    d[0]=n*2;
    fo(i,1,n)
        if(!c[i])dfs(i,1);
    if(s1%3!=0)
    {
        if(s1%3!=1)rev();
        if(!solve())
        {
            s=0;
            memset(ans,0,sizeof ans);
            rev();
            if(!solve()||!solve()){printf("NO\n");return 0;}
        }
    }
    printf("YES\n");
    fo(i,1,n)if(c[i]==1&&!ans[i])ans[i]=++s;
    fo(i,1,n)if(c[i]==2&&!ans[i])ans[i]=++s;
    fo(i,1,n-1)printf("%d ",(ans[i]-1)/3+1);
    printf("%d\n",(ans[n]-1)/3+1);
    return 0;
}