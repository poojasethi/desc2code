#include<iostream>
using namespace std;
long long ones[100],ans;
int o(int x)
{
    int br=0;
    while(x!=0)
    {
        if(x%2==1)br++;
        x/=2;
    }
    return br;
}
int main()
{
    int n,a;
    cin>>n;
    for(int i=1;i<=n;i++)cin>>a,ones[o(a)]++;
    for(int i=1;i<=50;i++)ans+=ones[i]*(ones[i]-1)/2;
    cout<<ans<<endl;
}
