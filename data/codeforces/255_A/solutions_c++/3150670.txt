#include<stdio.h>
int main()
{
int n,i,a[3]={0},x,mx=0,in;
scanf("%d",&n);
for(i=0;i<n;i++){
scanf("%d",&x);
a[i%3]+=x;
if(a[i%3]>mx){mx=a[i%3]; in=i%3;}
}
if(in==0) puts("chest");
else if(in==1) puts("biceps");
else puts("back");
return 0;
}