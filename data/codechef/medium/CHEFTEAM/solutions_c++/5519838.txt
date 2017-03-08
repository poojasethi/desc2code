#include <bits/stdc++.h>
#define gcd __gcd
#define ull unsigned long long
#define INFULL 0xffffffffffffffff
using namespace std;
ull C[100][100]; // stores value only if it in range of ull
void precompute()
{
    for(int i=0;i<100;i++)
    {
        C[i][0] = C[i][i] = 1;
        for(int j=1;j<i;j++)
        {
            //if(((INFULL - C[i-1][j-1]) < C[i-1][j])){C[i][j] = 0;break;}  //check overflow
            C[i][j] = C[i-1][j] + C[i-1][j-1];
        }
    }
    //cout<<C[20][10]<<endl;
}
ull comb(ull n,ull r)
{
    ull temp,x,y;
    if(n<r)return 0;
    if(n-r < r)r = n-r;
    ull ans = 1;
    for(ull i=1;i<=r;i++)
    {
        x = i;
        temp = gcd(ans,x);
        ans/=temp;x/=temp;
        y = n-i+1ULL;
        temp = gcd(y,x);
        y/=temp;x/=temp;
        ans*=y;
    }
    return ans;
}
int main()
{
    //precompute();
    int t;
    scanf("%d",&t);
    while(t--)
    {
        ull n,r;
        scanf("%llu%llu",&n,&r);
        printf("%llu\n",comb(n,r));
    }
}
