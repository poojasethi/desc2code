#include<bits/stdc++.h>
using namespace std;
long long a[2000],b[2000],l,n,i;
int main()
{
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i]>>b[i];
    }
    sort(a,a+n);
    sort(b,b+n);
  l= max(abs(a[0]-a[n-1]),abs(b[0]-b[n-1]));
  cout<<l*l<<endl;



}
