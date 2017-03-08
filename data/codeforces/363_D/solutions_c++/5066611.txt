#include<bits/stdc++.h>
using namespace std;
int n,m,a;
int b[100009];
int p[100009];
int righ,lef,br,r;
long long chk(int x)
{
    long long cr=a;
    for(int i=1;i<=x;i++)
    {
        cr-=max(0,p[i]-b[n-x+i]);
    }
    return cr;
}
int main()
{
    cin>>n>>m>>a;
    for(int i=1;i<=n;i++)cin>>b[i];
    for(int j=1;j<=m;j++)cin>>p[j];
    sort(b+1,b+n+1);
    sort(p+1,p+m+1);
    int mid;
    lef=0;
    righ=min(n,m)+1;
    while(righ-lef>1)
    {
        //cout<<lef<<" "<<righ<<endl;
        mid=(lef+righ)/2;
        if(chk(mid)>=0)lef=mid;
        else righ=mid;
    }br=lef;
    for(int i=1;i<=br;i++)r+=p[i];

    r=max(0,r-a);
    cout<<br<<" "<<r<<endl;
}
