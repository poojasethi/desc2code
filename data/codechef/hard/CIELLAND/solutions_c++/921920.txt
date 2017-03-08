#include<stdio.h>
#include<math.h>
short tab[8200][4200];
int c[20];
double a[14][8200];
double b[14][2],d[20];

inline double max(double o,double p)
{
    if (o>p) return o;return p;
}

inline double dis(int o,int p)
{
    return sqrt((b[o][0]-b[p][0])*(b[o][0]-b[p][0])+(b[o][1]-b[p][1])*(b[o][1]-b[p][1]))/2.0;
}

inline double min(double o,double p)
{
    if (o<p) return o;return p;
}

double mul(double x1,double y1,double x2,double y2)
{
    return x1*y2-x2*y1;
}

inline double calc()
{
    double ans=-1;
    if (c[0]<3) return 0;
    for (int i=1;i<=c[0];i++)
     for (int j=1;j<=c[0];j++)
     if (i!=j)
     {
         bool u=true;
         for (int k=1;k<=c[0];k++)
         if ((i!=k)&&(j!=k))
         {
             d[k]=mul(b[c[k]][0]-b[c[i]][0],b[c[k]][1]-b[c[i]][1],b[c[j]][0]-b[c[i]][0],b[c[j]][1]-b[c[i]][1]);
             if (d[k]<-1e-10) u=false;
         }
         if (u)
         {
             double tmp=0,ed=dis(c[i],c[j]);
             for (int k=1;k<=c[0];k++)
             if ((i!=k)&&(j!=k)) tmp=max(tmp,(d[k]/ed)/4.0);
             if (ans<0) {ans=tmp;} else {ans=min(tmp,ans);}
         }
     }
    return ans;
}

int main()
{
    for (int i=1;i<(1<<13);i++)
    {
        tab[i][0]=0;
        for (int j=1;j<(1<<13);j++)
        if ((i&j)==0)
        {
            tab[i][0]++;
            tab[i][tab[i][0]]=j;
        }
    }

    int tt;scanf("%d",&tt);
    while (tt>0)
    {
        tt--;
        int n,k;
        scanf("%d%d",&n,&k);
        for (int i=0;i<n;i++) scanf("%lf%lf",&b[i][0],&b[i][1]);
        c[0]=0;
        for (int i=1;i<=k;i++)
        for (int j=1;j<(1<<n);j++) a[i][j]=-1;
        for (int i=1;i<(1<<n);i++)
        {
            c[0]=0;
            for (int j=0;j<n;j++)
            if ((i&(1<<j))!=0)
            {
                c[0]++;
                c[c[0]]=j;
            }
            a[1][i]=calc();
        }
        for (int i=1;i<k;i++)
        for (int j=1;j<(1<<n);j++)
        if (a[i][j]>=0)
        {
            if (i!=1) a[i][j]=min(a[i-1][j],a[i][j]);
            for (int k=1;k<=tab[j][0];k++)
            {
                int st=(tab[j][k]|j);
                if (a[i+1][st]<0) {a[i+1][st]=max(a[i][j],a[1][tab[j][k]]);}
                else
                {
                    a[i+1][st]=min(a[i+1][st],max(a[i][j],a[1][tab[j][k]]));
                }
            }
        }
        for (int i=1;i<k;i++) a[k][(1<<n)-1]=min(a[k][(1<<n)-1],a[i][(1<<n)-1]);
        printf("%.6f\n",a[k][(1<<n)-1]);
    }
    return 0;
}
