#include <stdio.h>

int a[100005];
bool vis[100005];
int main()
{
    int i,n;
    scanf("%d", &n);
    if(n&1)
        return puts("-1") , 0;
    a[n] = 0;
    a[n-1] = n/2;
    vis[n/2] = 1;
    for(i = n-1;i > 0 ; i--) {
        int x1 = a[i]/2;
        int x2 = (a[i]+n)/2;
        if(vis[x1])
            a[i-1] = x2 , vis[x2] = 1;
        else if(vis[x2])
            a[i-1] = x1 , vis[x1] = 1;
        else if(x1 > x2)
            a[i-1] = x1 , vis[x1] = 1;
        else
            a[i-1] = x2 , vis[x2] = 1;
    }
    for(i = 0;i <= n; i++)
        printf("%d ", a[i]);
    puts("");
    return 0;
}