#include <iostream>
using namespace std;
int main()
{
int i,j,n,m;
char a,b;
cin>>n>>m; b=-1;
for (i=0;i<n;i++)
{
    cin>>a; if (a==b) {cout<<"NO"; return 0;}
    for (j=1;j<m;j++)
    {
        cin>>b; if (b!=a) {cout<<"NO"; return 0;}
    }
}
cout<<"YES";
return 0;
}