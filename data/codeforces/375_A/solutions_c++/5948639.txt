#include<bits/stdc++.h>
using namespace std;
typedef unsigned long LL;
LL DIG[10],DIV[7]={1869,6198,1896,1689,1986,1968,1698},m,i;
int main()
{
    char c;
    while((c=getchar())>0)if(c>='0')DIG[c-'0']++;
    DIG[1]--;DIG[8]--;DIG[6]--;DIG[9]--;
    for(i=10;--i;)while(DIG[i]--){m=(m*3+i)%7;putchar('0'+i);}
    printf("%u",DIV[m]);
    while(DIG[0]--)putchar('0');
    putchar('\n');
    return 0;
}