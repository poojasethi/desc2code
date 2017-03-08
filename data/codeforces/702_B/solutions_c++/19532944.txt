#include <cstdio>
#include <map>
using namespace std;
map <long long,int> arr;
int main()
{
    int n,a;
    long long ans=0;
    scanf("%d",&n);
    while(n--)
    {
        scanf("%d",&a);
        for(int i=1; i<=31; i++)
            ans+= arr[(1ll<<i)-a];
        arr[a]++;
    }
    printf("%I64d",ans);
    return 0;
}
