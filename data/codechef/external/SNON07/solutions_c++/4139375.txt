#include<stdio.h>
int main()
{
    long long int n,m;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %lld",&n,&m);
        if(n%2==0&&m%2==0)
        {
            if(n>m)
                printf("U\n");
            else if(m>=n)
                    printf("L\n");
        }
        else if(n%2!=0&&m%2!=0)
        {
            if(n>m)
                printf("D\n");
            else if(m>=n)
                printf("R\n");
        }
        else
        {
            if(n%2==0&&m%2!=0)
                {
                    if(n>m)
                        printf("D\n");
                    else
                        printf("L\n");
                }
            if(n%2!=0&&m%2==0)
                {
                    if(n<m)
                        printf("R\n");
                    else
                        printf("U\n");
                }
        }
    }
    return 0;
}