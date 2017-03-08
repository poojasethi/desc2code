#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
long long l,r;

int main()
{
    cin>>l>>r;        
    long long a=1;
    do
    {a*=10;}
    while(a<=r);
    long long p=a/2;
    if(l<=p)
    {
        if(p<=r)
        cout<<p*(a-1-p);
        else 
        {
            cout<<r*(a-1-r);    
        }    
    }
    else 
    {
        cout<<l*(a-1-l);    
    }
    //cin>>l;
}
