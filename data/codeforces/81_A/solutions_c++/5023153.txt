#include<cstdio>
int main()
{int i=0;
char c,s[300000];
c=getchar();
while(c!='\n')
{
if(i<=0||s[i-1]!=c)
s[i++]=c;
else i--;
c=getchar();
}s[i]='\0';
puts(s);return 0;}