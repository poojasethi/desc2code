#include<stdio.h>
char a[1005][1005],s[1005][1005];
int main()
{
    int n,m,i,j,c;
    bool ok=1;
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)scanf("%s",a[i]+1);
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)s[i][j]='.';
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
        {
            if(a[i][j]!='b')continue;
            c='a'+2*((i/2+j/2)%2)+i%2;
            if(a[i-1][j]=='w'&&a[i+1][j]=='w'){s[i-1][j]=s[i][j]=s[i+1][j]=c;a[i-1][j]=a[i][j]=a[i+1][j]='.';}
            else if(a[i][j-1]=='w'&&a[i][j+1]=='w'){s[i][j-1]=s[i][j]=s[i][j+1]=c;a[i][j-1]=a[i][j]=a[i][j+1]='.';}
        }
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)if(a[i][j]!='.')ok=0;
    if(ok)
    {
        printf("YES\n");
        for(i=1;i<=n;i++,putchar('\n'))
            for(j=1;j<=m;j++)putchar(s[i][j]);
    }else printf("NO\n");
    return 0;
}