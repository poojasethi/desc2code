#include<bits/stdc++.h>
using namespace std;

int main() {

    ios_base::sync_with_stdio(0);
    int i,r,j,a[21],t,n;
    cin>>t;
    while(t--)
    {
        int c[21]={1};
    cin>>n;
    for(i=0;i<n;i++)cin>>a[i];
    for(i=1;i<n;i++)
    {
        r=INT_MIN;
        for(j=0;j<i;j++)
        {
            r=c[j];
            if(a[i]>a[j])c[i]=max(c[i],1+r);
        }
        c[i]=max(1,c[i]);
    }
    r=INT_MIN;
    for(i=0;i<n;i++)
    {
        r=max(r,c[i]);
    }
    cout<<r<<endl;
    }
    return 0;
}
