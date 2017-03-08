#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    if(k*3 > n) printf("-1\n");
    else
    {
        for(int i=0;i<k;i++) printf("%d ", 1+((i+1)%k));
        for(int i=k;i<n;i++) printf("%d ", 1+(i%k));
    }
    return 0;
}
