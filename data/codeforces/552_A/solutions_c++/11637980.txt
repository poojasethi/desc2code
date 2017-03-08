#include<iostream>
using namespace std;
int n,a,b,c,d,s,i;
int main()
{
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cin>>a>>b>>c>>d;
        s+=(d-b+1)*(c-a+1);
    }
    cout<<s;
}
