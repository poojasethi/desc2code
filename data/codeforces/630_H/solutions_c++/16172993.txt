#include <iostream>

using namespace std;
long long n,s;
int main()
{
    cin>>n;
    s=n*(n-1)*(n-2)*(n-3)*(n-4);
    s*=n*(n-1)*(n-2)*(n-3)*(n-4)/2/3/4/5;
    cout<<s;
}
