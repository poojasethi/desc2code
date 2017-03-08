#include <cstdio>
int main()
{
    int st=3,ans=0,a,n;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d",&a);
        if(st==1) st=2;
        else if(st==2) st=1;
        if((a&st)==0)
        {
            st=3;
            ans++;
        }
        else
            st&=a;
    }
    printf("%d",ans);
    return 0;
}
