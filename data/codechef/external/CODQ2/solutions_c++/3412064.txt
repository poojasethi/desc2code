#include <iostream>
#include <math.h>
#include <cstdio>
using namespace std;

int main()
{
    int n,temp,i,j,a5,a3,a2,a1;
    cin>>n;
    a5=n/5;
    if(n/5)n=n-(5*a5);
    a3=n/3;
    if(n/3)n=n-(3*a3);
    a2=n/2;
    if(n/2)n=n-(2*a2);
    a1=n/1;
    if(n/1)n=n-(1*a1);
    cout<<a5<<endl<<a3<<endl<<a2<<endl<<a1<<endl;
    return 0;
}
