#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
  int c1,c2,c3,c4,n,m,a=0,b=0,x;
  cin>>c1>>c2>>c3>>c4>>n>>m;
  while(n--)
  {scanf("%d",&x);a+=min(c1*x,c2);}
  while(m--)
  {scanf("%d",&x);b+=min(c1*x,c2);}
  a=min(a,c3);b=min(b,c3);
  printf("%d\n",min(c4,a+b));
}