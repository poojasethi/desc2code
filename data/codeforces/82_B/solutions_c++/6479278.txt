#include <stdio.h>

using namespace std;

int main()
{
    int n,m,x;
    int a[205][205]={0};
    int chk[205]={0},b[205]={0};
    scanf("%d",&n);
    if(n==2)
    {
        int x;
        scanf("%d%d",&m,&x);
        printf("1 %d\n%d ",x,m-1);
        for(int j=1;j<m;j++)
        {
            scanf("%d",&x);
            printf("%d ",x);
        }
        return 0;
    }
    for(int i=0;i<n*(n-1)/2;i++)
    {
        scanf("%d",&m);
        for(int j=0;j<m;j++) scanf("%d",&b[j]);
        for(int j=0;j<m;j++)
        {
            a[b[j]][b[j]]++;
            for(int k=j+1;k<m;k++) a[b[j]][b[k]]++,a[b[k]][b[j]]++;
        }
    }
    for(int i=1;i<=200;i++)
    {
        int cnt=0;
        for(int j=1;j<=200;j++) if(a[i][j]==n-1&&chk[j]==0) cnt++,chk[j]=1;
        if(cnt>0)
        {
            printf("%d ",cnt);
            for(int j=1;j<=200;j++) if(a[i][j]==n-1) printf("%d ",j);
            printf("\n");
        }
    }
    return 0;
}
