#include<stdio.h>
int main()
{
    int cases;
    scanf("%d", &cases);
    while(cases--)
    {
        long long int ans = 1;
        int n;
        long int a;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%ld", &a);
            ans *= a;
            ans = ans % 1000000007;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
