#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long n,a,b,p,q,sum,lcm;
    while(cin>>n){
        cin>>a>>b>>p>>q;
        lcm=(a*b)/__gcd(a,b);
        sum=(n/a)*p+(n/b)*q-(n/lcm)*(min(p,q));
        cout<<sum<<endl;
    }
}
