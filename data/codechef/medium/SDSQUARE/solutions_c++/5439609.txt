#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<sstream>
using namespace std;

int main()
{
    long long int t,i,j,a,b,flag,x,n;
     vector<long long int> square;
     int index=0;
     for(i=1;i<=100000;i++)
   {
       flag=0;
       x=i*i;
       n=x;
       while(n)
       {
           int temp=n%10;
           if(temp==2||temp==3||temp==5||temp==6||temp==7||temp==8)
           {
               flag=1;
               break;
           }
           n=n/10;
       }
       if(flag==0)
        square.push_back(x);
   }
    scanf("%lld",&t);
   while(t--)
   {
       scanf("%lld%lld",&a,&b);
       printf("%d\n",lower_bound(square.begin(),square.end(),b+1)-lower_bound(square.begin(),square.end(),a));
   }
    return 0;
}
