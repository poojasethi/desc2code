#include<bits/stdc++.h>
using namespace std;
long long n,i,a[300005],sum;
int main()
{
    cin>>n;
    for(i=1;i<=n;i++)
    cin>>a[i];
    sort(a+1,a+n+1);
    for(i=1;i<=n;i++)
    sum+=abs(a[i]-i);
    cout<<sum<<endl;


}
