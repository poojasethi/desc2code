#include <iostream>

using namespace std;

int main()
{
    int n,mx,mn;
    cin>>n;
    mx=mn=n/7*2;
    n-=n/7*7;
    mn+=max(0,n-5);
    mx+=min(2,n);
    cout<<mn<<' '<<mx;
}
