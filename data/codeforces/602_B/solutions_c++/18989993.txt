#include <cstdio>
#include <algorithm>
using namespace std;
int pos[100005];
int main()
{
    int n,ans=0,k;
    scanf("%d",&n);
    for(int i=1 ; i<=n; i++)
    {
        scanf("%d",&k);
        pos[++k] = i;
        ans = max(ans,i-max(min(pos[k-1],pos[k+1]),max(pos[k-2],pos[k+2])));
    }
    printf("%d",ans);
    return 0;
}
