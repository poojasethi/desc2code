#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
using namespace std;
typedef long long LL;
const LL Mod=1000000007ll;
LL num[50];
LL Pow(LL a,LL b,LL mod){
    LL ans=1;
    while(b){
        if(b&1) b--,ans=(ans*a)%mod;
        else b/=2,a=(a*a)%mod;
    }
    return ans%mod;
}
int main(){
    int T;
    scanf("%d",&T);
    while(T--){
        int up,d,N,m;
        scanf("%d%d%d%d",&up,&d,&m,&N);
        for(int i=0;i<N;i++) num[i]=up/N+(up%N>=i);
        //for(int i=0;i<10;i++) cout<<i<<" "<<num[i]<<endl;
        LL ans=0;
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                for(int k=0;k<N;k++){
                    LL tmp=0;
                    tmp+=Pow(i,d,N);
                    tmp+=Pow(j,d,N);
                    tmp+=Pow(k,d,N);
                    if(tmp%N==m){
                        LL cnt=1;
                        cnt=(cnt*num[i])%Mod;
                        cnt=(cnt*num[j])%Mod;
                        cnt=(cnt*num[k])%Mod;
                        ans=(ans+cnt)%Mod;
                    }
                }
        printf("%lld\n",ans%Mod);
    }
    return 0;
}
