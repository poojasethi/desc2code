#include <cstdio>
int main()
{
    long long n;
    scanf("%I64d",&n);
    printf("%I64d",(1ll<<(n+1))-2ll);
    return 0;
}
