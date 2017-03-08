#include <cstdio>
char A[10]="hello",a;
int i;
main()
{while(scanf("%c",&a) && a!='\n')
if(a == A[i])i++;
printf(i==5 ? "YES" : "NO");}
