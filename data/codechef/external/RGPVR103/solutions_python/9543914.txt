#include<stdio.h>

using namespace std;

int main()
{
    long int t;
    scanf("%ld",&t);
    while(t--)
    {
        long int n,x,y;
        scanf("%ld",&n);

    x=(n/4);
    y=n/2;
    y=(y-x);
    printf("%ld\n",x*y);
    }
}
