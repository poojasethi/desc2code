#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
int main ()
{
    char ch[10];
    while (scanf("%s",ch)!=EOF)
    {
        int i,ans,n,e;
        n=10*(ch[0]-'0')+ch[1]-'0';
        e=ch[3]-'0';
        if(!(n||e))break;
        while (e--)
         n*=10;
        int c=1;
        while (c<=n)
         c<<=1;
        ans=((n-(c>>1))<<1)+1;
        printf("%d\n",ans);
    }
    return 0;
}