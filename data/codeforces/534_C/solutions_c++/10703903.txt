#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int N=100001;
int main()
{
  ll n,A,sum=0;
  cin>>n>>A;
  ll a[2*N];
  for(int i=0;i<n;i++){cin>>a[i];sum+=a[i];}
  for(int i=0;i<n;i++)
  {
      int p=max(0ll,A-(sum-a[i])-1);
      int q=max(0ll,n-1+a[i]-A);
      cout<<p+q<<" ";
  }


    return 0;
}
