#include<limits.h>
#include<math.h> 
#include<stdbool.h>
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
int main() 
{
 long t,i,k,n,j,l;
 bool a[30][30];
 char map[5],s[10000],p[10000];
 bool val;
 scanf("%ld",&t);
 while(t--)
 {
    val=true;
    for(i=0;i<30;i++)
    {
        for(j=0;j<30;j++)
        {
        a[i][j]=false;
      //  printf("%c ",a[i][j]);
        }
        a[i][i]=true;
        //printf("\n");
    }
    scanf("%s",s);
    scanf("%s",p);
    scanf("%ld",&n);
    while(n--)
    {
        scanf("%s",map);
        k=map[0];
        l=map[3];
        a[k-97][l-97]=true;
    }
    for(k=0;k<26;k++)
    for(i=0;i<26;i++)
    for(j=0;j<26;j++)
    {
        if(a[i][k] & a[k][j])
        a[i][j]=true;
    }
    /***
    for(i=0;i<26;i++)
    {
        for(j=0;j<26;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    } */
    if(strlen(s)!=strlen(p))
    val=false;
    else 
    {
        for(i=0;i<strlen(s);i++)
        {
                k=s[i]-97;
                l=p[i]-97;
                if(a[k][l]==false)
                {
                    val=false;
                    break;
                }
        }
    }
    if(val==true)
    printf("YES\n");
    else 
    printf("NO\n");
 }
	return 0;
}