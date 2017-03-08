// by ξ

#include <cstdio>
#include <cstdlib>

using namespace std;

int n,i,j,k,ans,a[200005];

int main(){
    scanf("%d",&n);
    for(i=1;i<=n;++i)scanf("%d",a+i);
    for(i=1;i<=n;){
        ++ans;
        for(j=i;a[j]==-1;++j);
        for(k=j+1;a[k]==-1;++k);
        if(k>n){printf("%d\n",ans);return 0;}
        long long dx=(a[k]-a[j])/(k-j),rem=a[k];
        if(1ll*(a[k]-a[j])%(k-j) || a[j]-1ll*(j-i)*dx<=0){i=k;continue;}
        for(i=k+1;i<=n && (a[i]==rem+dx || a[i]==-1) && rem+dx>0;++i,rem+=dx);
    }
    printf("%d\n",ans);
}