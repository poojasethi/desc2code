#include<stdio.h>
int main()
{
    bool seen[1007] = {false};
    int cases;
    scanf("%d",&cases);
    long long int n;
    while(cases--)
    {
        scanf("%lld", &n);
        int a = n%1007;
        if(!seen[a])
        {
            printf("%d\n", a);
            seen[a] = true;
        }
    }
    return 0;
}
