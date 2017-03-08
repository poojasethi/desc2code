#include <iostream>
#include <cmath>
using namespace std;
int n;
int main()
{
    cin>>n;
    while(n)
    {
        cout<<floor(log2(n))+1<<' ';
        n-=pow(2,floor(log2(n)));
    }
}
