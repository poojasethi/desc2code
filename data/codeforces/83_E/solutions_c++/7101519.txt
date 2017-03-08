#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n,m;
int num[200010],f[1048576][21],cf[21];
char ch[30];
int sum,tmp;
int main()
{
    int i,j,k;
    scanf("%d\n",&n);
    for(i=1;i<=n;i++)
    {
       gets(ch+1);
       m=strlen(ch+1);
       for(j=1;j<=m;j++)
       {
        num[i]=(num[i]<<1)+(ch[j]-'0');
       }
    }
    cf[0]=1;
    for(i=1;i<=20;i++)
    cf[i]=cf[i-1]*2;
    memset(f,0xC0,sizeof(f));
    for(i=2;i<=n;i++)
    {
     for(k=m;k>=1;k--)
     if((num[i-1] & cf[k]-1) == (num[i]>>m-k))  break;
     sum+=k;tmp=0;
     for(j=0;j<=m;j++)  tmp=max(tmp,f[num[i]>>m-j][j]+j);
     for(j=0;j<=m;j++)  f[num[i-1] & cf[j]-1][j]=max(f[num[i-1] & cf[j]-1][j],tmp-k);  
    }
    tmp=0;
    for(j=0;j<=m;j++)
    for(i=0;i<=cf[j]-1;i++)
    tmp=max(tmp,f[i][j]);
    printf("%d\n",n*m-sum-tmp);
    return 0;
}
