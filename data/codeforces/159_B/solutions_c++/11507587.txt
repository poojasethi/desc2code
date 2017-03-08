#include<bits/stdc++.h>
using namespace std;
int v[1003][1003],c[1003],i,n,m,x,y,a,b;
main()
{
    scanf("%d%d",&n,&m);
    for (i=0;i<n;i++)
    {
        scanf("%d%d",&x,&y);
        v[x][y]++;
        c[y]++;
    }
    for (i=0;i<m;i++)
    {
        scanf("%d%d",&x,&y);
        if (v[x][y]) b++,v[x][y]--;
        if (c[y]) a++,c[y]--;
    }
    printf("%d %d",a,b);
}
