#include<cstdio>
#include<cstring>
int main()
{
    char a[109],i;
    gets(a);
    for(i=1;i<strlen(a)+1;i++)
    {
        if(a[i-1]==' '&&a[i]==' ')
        {
            continue;
        }
        else
        {
            printf("%c",a[i-1]);
        }
    }
    return 0;
}
