#include <cstdio>
int main()
{
    int n;
    scanf("%d",&n);
    for(int c=0;c<n;c++)
        printf("%c",'a'+(c%4));
}