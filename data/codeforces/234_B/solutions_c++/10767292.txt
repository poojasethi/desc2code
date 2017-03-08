#include <iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int n,k,i;
main()
{
pair<int,int> a[1005];
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
cin>>n>>k;
for(i=0;i<n;i++)
{
cin>>a[i].first;
a[i].second=i+1;
}
sort(a,a+n);
cout<<a[n-k].first<<endl;
for(i=n-k;i<n;i++)
cout<<a[i].second<<" ";
}