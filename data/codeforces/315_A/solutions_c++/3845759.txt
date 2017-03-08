#include<iostream>
using namespace std;
int a[1000],b[1000],br,n;
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)cin>>a[i]>>b[i];
    for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)
    {
        if(a[i]==b[j]&&i!=j)break;
        if(j==n)br++;
    }
    cout<<br<<endl;
}
