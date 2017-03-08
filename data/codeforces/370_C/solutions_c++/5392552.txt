#include <stdio.h>
#include <algorithm>
using namespace std;

int inp[5002];

int main()
{
    int n,m,i,r;

    scanf("%d%d",&n,&m);

    for(i = 0; i < n; i++)
    {
        scanf("%d",inp + i);
    }

    sort(inp,inp + n);

    r = n;

    for(i = 0; i < n; i++)
    {
        if(inp[i] == inp[(i + n / 2) % n])
        {
            r--;
        }
    }

    printf("%d\n",r);

    for(i = 0; i < n; i++)
    {
        printf("%d %d\n",inp[i],inp[(i + n / 2) % n]);
    }
}
