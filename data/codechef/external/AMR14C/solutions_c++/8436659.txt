#include<bits/stdc++.h>
using namespace std;
int a[100100];
int ntest;
int n,M,X;
long long T[300100];

int main()
{
    ios::sync_with_stdio(false);
    cin>>ntest;
    for (int kk = 1; kk<=ntest; kk++)
    {
       cin>>n>>M>>X;
       memset(T,0,sizeof(T));
       for (int i = 1; i<=n; i++)
       {
           cin>>a[i];
           a[i] = a[i]%M;
           T[a[i]]++;
       }

       for (int i = 1; i<= M + X; i++)
           T[i] = T[i-1] + T[i];
       long long ans = 0;
       for (int i = 1; i<=n; i++)
       {
           if (X >= a[i])
               ans = ans + T[X - a[i]];
           ans = ans + (T[M+X-a[i]] - T[M-1-a[i]]);
       }
       cout<<ans<<"\n";
    }
    return 0;
}