#include<iostream>

using namespace std;

int main()
{
    int n,k;
    cin>>n>>k;
    int u,l = 0;
    int ans = 0;
    int c;
    cin>>c;
    for (int i=0;i<c;i++)
    {
        cin>>u;
        ans += (u - l - 1) / k;
        ans++;
        l = u;
    }
    cout<<ans + (n - l) / k<<endl;
    return 0;
}