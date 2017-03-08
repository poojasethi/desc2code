#include <stdio.h>
int main()
{
int n,x,y;
scanf("%d%d%d",&n,&x,&y);
x=(y*n+99)/100-x;
printf("%d",x<=0?0:x);
}