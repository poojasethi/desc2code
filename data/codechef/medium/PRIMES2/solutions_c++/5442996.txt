#include<cstdio>
#include<iostream>
using namespace std;

int isprime(int n)
{
    if(n<2||(!(n&1)&&n!=2))
    {
        return 0;
    }
    for(int i=3;i*i<=n;i=i+2)
    {
        if(n%i==0)
            return 0;
    }
    return 1;
}
int main()
{
    int n,p1=0,p2=0,p3=0;
    scanf("%d",&n);
    while(n!=0)
    {
        int flag=0;
        for(p3=97;p3>=2;p3--)
        {
            if(p3*p3*p3<n&&isprime(p3))
            {
                for(p2=2;p2*p2+p3*p3*p3<n;p2++)
                {
                    p1=n-p3*p3*p3-p2*p2;
                    if(isprime(p1)&&isprime(p2))
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                    break;
            }
        }
        if(flag==1)
            printf("%d %d %d\n",p1,p2,p3);
        else
            printf("0 0 0\n");
        scanf("%d",&n);
    }
    return 0;
}
