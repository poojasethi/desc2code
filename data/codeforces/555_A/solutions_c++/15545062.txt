#include <stdio.h>
int main()
{
    int n,m,k,a;
    scanf("%d%d",&n,&m);
    int ans=2*n-m+1;
    while (m--)
    {
        scanf("%d",&k);
        for (int i=1;i<=k;i++)
        {
            scanf("%d",&a);
            if (a==i)
                ans-=2;
        }
    }
    printf("%d",ans);
    return 0;
}
