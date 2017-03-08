#include<iostream>
#include<bits/stdc++.h>
using namespace std;
long long int cuspow10(long long int  exp)
    {
        long long int  ans =1 ;
        long long int  base = 10;
        while(exp!=0)
        {
            if(exp%2==1)ans = ans*base;
            base = base*base;
            exp/=2;
        }
        return ans;
    }
long long int MOD(long long int base, long long int MOD)
{
        long long int exp = base;
        long long int  ans = 1;
        base = base%MOD;
        while(exp!=0)
        {
            if(exp%2==1)ans = (ans*base)%MOD;
            base = (base*base)%MOD;
            exp/=2;
        }
        for(MOD/=10;MOD>1 && MOD>=ans;MOD/=10)
        {
            cout<<0;
        }
        return ans;
}
long long int firstNdigits(long long int base, long long int MOD)
{
    long double x = base*log10l(base);
    long double y = powl(10,x-(int)x);
    long long int ans = y*MOD;
    return ans;
}
int main()
{
    int T, N, POW;
    cin>>T;
    while(T--)
    {
        cin>>N>>POW;
        cout<<firstNdigits(N,cuspow10(POW-1))<<" ";
        cout<<MOD(N,cuspow10(POW))<<"\n";
    }
    return 0;
}
