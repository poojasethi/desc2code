#include<iostream>
#include<bits/stdc++.h>
typedef unsigned long long int ULLI;
using namespace std;
int main()
{
    ULLI T, N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        ULLI ans = 5*N*N;
        ULLI ans1 = ans+4;
        ans-=4;
        ULLI sq = sqrt(ans);
        ULLI sq1 = sqrt(ans1);
        if(sq*sq==ans || sq1*sq1==ans1)cout<<"Yes\n";
        else cout<<"No\n";
    }
    return 0;
}
