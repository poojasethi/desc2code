#include <cstdio>
int main()
{
    char s[20];
    int t,a,i;
    scanf("%d",&i);
    for(t=0;t<i;t++)
    {
        scanf("%s",s);
        scanf("%s",s);
        scanf("%d",&a);
        if(a>200)
        {
            printf("%d\n",t+1);
        }
    }
    return 0;
}
