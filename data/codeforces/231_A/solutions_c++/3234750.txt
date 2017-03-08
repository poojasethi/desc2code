#include <iostream>
using namespace std;
int main()
{
int a,b,c,ans=0;
cin>>a;
while(cin>>a>>b>>c)
if(a+b+c>=2)
ans++;
cout<<ans; return 0;}