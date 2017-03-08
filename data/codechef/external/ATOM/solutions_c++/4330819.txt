#include<iostream>
#include<cmath>
#include<stdio.h>
typedef unsigned long long int ULLI;
using namespace std;
int main()
{
    long double P, N, K, M;
    long double ANS, PROD;
    cin>>P;
    while(P--)
    {
        cin>>N>>K>>M;
        ANS = 0;
        PROD = N*K;
        while(PROD<=M)
        {
            PROD = PROD * K;
            ++ANS;
        }
        cout<<ANS<<"\n";
    }
    return 0;
}
