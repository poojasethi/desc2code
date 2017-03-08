#include<bits/stdc++.h>
using namespace std;
int count_bits (int n)
{
    int c=0,a;
    while(n!=0)
    {
        a = n%2;
        if(a==1)
            c++;
        n = n/2;
    }
    return c;
}
int main()
{
    int i,j,k,l,m,n,tc,ans;
    while(cin>>tc)
    {
        for(l=1;l<=tc;l++)
        {
            ans=0;
            cin>>n;
            for(i=1;i<=n;i++)
            {
                ans+=count_bits(i);
            }
            cout<<ans<<endl;
        }
    }

    return 0;
}
