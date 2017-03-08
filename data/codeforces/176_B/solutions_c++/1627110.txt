#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
#define ll long long
const ll MOD=1000*1000*1000+7;
ll ans,cnt,K,f[2][2];
string a,b;

int main()
{
    cin>>a>>b>>K;
    int l=a.size();
    f[0][a==b]=1;
    a=a+a;
    for(int i=0;i<l;i++) if(a.compare(i,l,b)==0) cnt++;
    for(int i=0;i<K;i++)
    {
        f[i&1^1][1]=(f[i&1][1]*(cnt-1)+f[i&1][0]*cnt)%MOD;
        f[i&1^1][0]=(f[i&1][1]*(l-cnt)+f[i&1][0]*(l-cnt-1))%MOD;
    }
    cout<<f[K&1][1]<<endl;
    return 0;
}