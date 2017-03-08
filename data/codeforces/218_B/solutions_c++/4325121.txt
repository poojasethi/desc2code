#include<bits/stdc++.h>
using namespace std;
int n,m;
int a[1009],b[1009];
int main()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        cin>>a[i];b[i]=a[i];
    }
    sort(a+1,a+m+1);
    int mn=0,mx=0;
    for(int i=1;i<=n;i++)
    {
        int k;k=0;
        while(a[k]==0)
        {
            k++;
        }
        mn+=a[k];a[k]--;
    }
    for(int i=1;i<=n;i++)
    {
        sort(b+1,b+m+1);reverse(b+1,b+m+1);mx+=b[1];b[1]--;
    }
    cout<<mx<<" "<<mn<<endl;
}

