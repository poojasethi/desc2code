#include <stdio.h>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int n,v[100],s=0;
    scanf("%d",&n);
    for(int i=0;i<n;++i)
        scanf("%d",&v[i]);
    sort(v,v+n);
    for(int i=0;i<n;++i)
        s+=v[n-i-1]*v[n-i-1]*(i&1?-1:1);
    printf("%lf",acos(-1)*s);
    return 0;
}