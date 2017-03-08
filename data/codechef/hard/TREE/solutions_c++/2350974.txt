#include <iostream>
#include <stdio.h>
#define mod 1000000007
#include <cmath>

using namespace std;

long long int power(long long int a, long long int b)
{
    long long result;
    if(b==1)
        return a;
    if(b==0)
        return 1;
    result = power(a,b/2)%mod;
    result=(result*result)%mod;
    if(b%2==1)
        result=(result*a)%mod;
    return result%mod;
}

int main()
{
    long long int n,k;
    scanf("%lld %lld",&n,&k);
    if(n<k)
    {
        cout<<"0"<<endl;
        return 0;
    }
    long long int temp1, temp2;
    temp1=(k*n);
    //cout<<temp1<<endl;
    temp1=power(temp1,n-2);
//    cout<<temp1<<endl;
    temp2=(k*(n-1));
//    cout<<temp2<<endl;
    temp2=power(temp2,(k-1)*n);
//    cout<<temp2<<endl;
    cout<<(temp1*temp2)%mod<<endl;
    return 0;
}
