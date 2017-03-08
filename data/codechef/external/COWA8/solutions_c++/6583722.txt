#include<iostream>
#include<string.h>
#include<cmath>
#include<cstdio>
using namespace std;
long long int arr[1000005],arra[1000005];
int main()
{
    int t,i,j,val = 0,s = 1,q,n;
    memset(arr,0,sizeof arr);
    t = sqrt(1000005);
    for(i = 2;i <= t;++i)
    {
        if(arr[i] == 0)
        {
            for(j = i*i;j <= 1000005;j = j+i)
            {
                arr[j] = 1;
            }
        }
    }
    for(i = 4;i <= 1000005;i++)
    {
        if(arr[i] == 0 && arr[i-2] == 0)
        {
            val = val+s;
            arra[i] = val;
        }
        else
        {
            arra[i] = val;
        }

    }
    scanf("%d",&q);
    while(q--)
    {
        scanf("%d",&n);
        if(n == 1||n==2||n==3)
            printf("0\n");
        else
            printf("%lld\n",arra[n]);
    }
    return 0;
}
