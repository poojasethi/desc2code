#include<bits/stdc++.h>
using namespace std;
int a[250];
#define ll long long
ll p[250],hsh[250];
#define MOD 1000000007
int main()
{
    int t,n,k;
    cin>>t;
    while(t--) {
        cin>>n>>k;
        for(int i=0;i<250;i++) {
            hsh[i]=0;
            p[i]=0;
        }
        for(int i=0;i<n;i++) {
            cin>>a[i];
            hsh[a[i]]++;
        }
        int m=0;
        p[0]=1;
        for(int i=200;i>=1;i--) {
            if(hsh[i]!=0) {
                int num=i;
                int N=hsh[i];
                ll t=1;
                for (int r = m + 1; r < m + N; ++r) t = (t*r)%MOD;
                ll val1=(t*N)%MOD,val2=(t*m)%MOD;
                 for(int i = k; i >= 0; --i)
                    {
                        p[i + 1] = (p[i + 1] + (val1 * p[i]) % MOD) % MOD;
                        p[i] = (p[i] * val2) % MOD;
                    }
                //p[0]=1;
                m+=N;
                //cout<<num<<" "<<p[1]<<endl;
            }
        }
        ll ans=0;
        for(int i=1;i<=k;i++) ans=(ans+p[i])%MOD;
        cout<<ans<<endl;
    }
    return 0;
}
