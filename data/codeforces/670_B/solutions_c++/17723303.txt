#include <iostream>

using namespace std;

int n,p,x,v[100100],i,x2;

int main()
{
    cin>>n>>p;
    for(i=1; i<=n; ++i)
        cin>>v[i];
    x=1;
    while(x<p)
    {
        p-=x;
        x++;
    }
    cout<<v[p];
}
