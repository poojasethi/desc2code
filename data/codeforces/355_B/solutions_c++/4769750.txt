#include<bits/stdc++.h>
using namespace std;
int c1,c2,c3,c4;
int n,m,s1,s2,s3,x;
int main()
{
    cin>>c1>>c2>>c3>>c4;
    cin>>n>>m;
    for(int i=1;i<=n;i++)
    {
        cin>>x;
        if(x*c1<c2)s1+=x*c1;
        else s1+=c2;
    }
    s1=min(s1,c3);
    for(int i=1;i<=m;i++)
    {
        cin>>x;
        if(x*c1<c2)s2+=x*c1;
        else s2+=c2;
    }
    s2=min(s2,c3);
    cout<<min(s1+s2,c4)<<endl;
}

