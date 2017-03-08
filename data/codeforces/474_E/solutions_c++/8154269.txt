#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
long long it[300005],p[100005],s[100005];
long long find(int x,int cl,int cr,int l,int r)
{
    if(l<=cl && cr<=r)return it[x];
    int o=0,c=0;
    if(l<=(cl+cr)/2)c=find(x*2,cl,(cl+cr)/2,l,r);
    if(s[o]<s[c])o=c;
    if(r>(cl+cr)/2)c=find(x*2+1,(cl+cr)/2+1,cr,l,r);
    if(s[o]<s[c])o=c;
    return o;
}
void up(int x,int l,int r,int i,int u)
{
    if(s[u]>s[it[x]])it[x]=u;
    if(l==r)return;
    if(i<=(l+r)/2)up(x*2,l,(l+r)/2,i,u);
    else up(x*2+1,(l+r)/2+1,r,i,u);
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    long long n,d,h[100005],o[100005],i,l,r,o1,o2,m;
    cin>>n>>d;
    for(i=1;i<=n;i++)
    {
        cin>>h[i];
        o[i]=h[i];
    }
    m=n;
    sort(o+1,o+n+1);
    for(i=n;i>0;i--)
    {
        o1=o2=0;
        r=lower_bound(o+1,o+n+1,h[i]+d)-o;
        l=upper_bound(o+1,o+n+1,h[i]-d)-o-1;
        if(r<=n)o1=find(1,1,n,r,n);
        if(l>=1)o2=find(1,1,n,1,l);
        if(s[o1]>s[o2])p[i]=o1;
        else p[i]=o2;
        s[i]=s[p[i]]+1;
        l=lower_bound(o,o+n+1,h[i])-o;
        up(1,1,n,l,i);
        if(s[i]>s[m])m=i;
    }
    cout<<s[m]<<'\n'<<m;
    int c=p[m];
    while(c)
    {
        cout<<" "<<c;
        c=p[c];
    }
    cout<<'\n';
}
