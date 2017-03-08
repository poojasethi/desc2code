#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;
typedef long long LL;
const int MN=3e5+7;
const int Mo=1e9+7;
int n,m,tot;
int d[MN],l[MN],r[MN],a[MN],b[MN];
vector <int> f[MN];

void dfs(int s){
    l[s]=++tot;
    for (int i=0; i<f[s].size(); i++){
        d[f[s][i]]=d[s]+1;
        dfs(f[s][i]);
    }
    r[s]=tot;
}

void add(int i,int u,int v){
    for (;i<=n;i+=i&-i){
        a[i]=(a[i]+u)%Mo;
        b[i]=(b[i]+v)%Mo;
    }
}

int get(int i,LL d){
    LL ans=0;
    for (;i;i-=i&-i)
        ans=(ans+a[i]+d*b[i])%Mo;
    return (ans+Mo)%Mo;
}

int main(){
    int i,j,k;
    scanf("%d",&n);
    for (i=2; i<=n; i++){
        scanf("%d",&k);
        f[k].push_back(i);
    }
    dfs(1);
    scanf("%d",&m);
    while (m--){
        scanf("%d",&k);
        if (k==1){
            int x,v,w;
            scanf("%d%d%d",&x,&v,&w);
            LL tmp=(v+(LL)d[x]*w);
            add(l[x],tmp%Mo,-w);
            add(r[x]+1,(-tmp)%Mo,w);
        }
        else{
            scanf("%d",&i);
            printf("%d\n",get(l[i],d[i]));
        }
    }
    return 0;
}