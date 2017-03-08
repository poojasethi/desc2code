#include <stdio.h>
const int mod=1000000007;
int c[1010][1010];
int main()
{
    int n,a,s=0;
    long long r = 1;
    scanf("%d",&n);
    for (int i=0; i<1010; i++)
    {
        c[i][0]=1;
        for (int j=1; j<=i; j++)
            c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod;
    }
    while(n--)
    {
        scanf("%d",&a);
        s+=a;
        r=(r*c[s-1][a-1])%mod;
    }
    printf("%d\n",r);
    return 0;
}
