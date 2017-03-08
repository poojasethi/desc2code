#include<bits/stdc++.h>
using namespace std;
int n,a,b,c,d;
int main()
{
    cin>>n;
    for(int i=1;i<=4;i++)
    {
        cin>>a>>b>>c>>d;
        if(min(a,b)+min(c,d)<=n)
        {
            cout<<i<<" "<<min(a,b)<<" "<<n-min(a,b)<<endl;
            return 0;
        }
    }
    cout<<-1<<endl;
}
