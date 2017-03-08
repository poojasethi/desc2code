#include<cstdio>
long long ans;
int n,m,t;

long long c(int n,int k){
    if(k>n-k)k=n-k;
    long long ans=1;
    for(int i=0;i<k;++i)ans*=(n-i),ans/=(i+1);
    return ans;
    }
int main(){
    scanf("%d%d%d",&n,&m,&t);
    ans=0;
    for(int i=4;i<=n && t-i>=1;++i)if(t-i<=m)ans+=c(n,i)*c(m,t-i);
    printf("%I64d\n",ans);
    }
