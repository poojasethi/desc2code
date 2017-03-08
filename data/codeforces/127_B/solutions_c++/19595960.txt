#include<iostream>
using namespace std;
int n,a,c[101],ans;
int main()
{
    cin>>n;
    while(n--)
    {
        cin>>a;
        c[a]++;
        if(c[a]%2==0)
            ans++;
    }
    cout<<ans/2;
}
