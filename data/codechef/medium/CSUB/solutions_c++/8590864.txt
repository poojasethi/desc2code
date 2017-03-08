#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t,n;
    string x;
    ll c;
    cin>>t;
    while(t--)
    {
        c=0;
        cin>>n;
        cin>>x;
        while(n--)
        {
            if(x[n]-48)c++;
        }
        c=(c*(c+1))/2;
        cout<<c<<endl;
    }
    return 0;
}
