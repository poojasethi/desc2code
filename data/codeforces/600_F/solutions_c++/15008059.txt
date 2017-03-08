#include <cstdio>
#include <algorithm>
#define repu(i,x,y) for (int i=x; i<=y; ++i)
using namespace std;

int a,b,m,u[100100],v[100100],l[1100][1100],r[1100][1100],x,y,ans,cntl[1100],cntr[1100],t1,t2,c[100100];

int main()
{
    scanf("%d%d%d",&a,&b,&m);
    repu(i,1,m)
    {
        scanf("%d%d",&u[i],&v[i]);
        ans=max(ans,max(++cntl[u[i]],++cntr[v[i]])),x=y=0;
        repu(j,1,ans)
        {
            if (!l[u[i]][j])
                x=j;
            if (!r[v[i]][j])
                y=j;
            if (x && y)
                break;
        }
        t2=i;
        for (int j=0; j&1 && t1 || !(j&1) && t2; j^=1)
            if (j)
                t2=l[u[t1]][y],l[u[t1]][y]=r[v[t1]][y]=t1,r[v[t2]][y]=0;
            else
                t1=r[v[t2]][x],l[u[t2]][x]=r[v[t2]][x]=t2,l[u[t1]][x]=0;
    }
    repu(i,1,max(a,b))
        repu(j,1,ans)
            c[l[i][j]]=c[r[i][j]]=j;
    printf("%d\n",ans);
    repu(i,1,m)
        printf("%d ",c[i]);
    return 0;
}