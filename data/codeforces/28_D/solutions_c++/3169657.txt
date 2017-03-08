#include<cstdio>
#include<map>
using namespace std;
#define N 100011

map<int ,int> g[N];
int f[N],ans[N],cnt,p[N],sum;

int main(void) {
    int n,v,c,l,r;
    scanf("%d",&n);
    for(int i=1;i<=n;++i) {
        scanf("%d%d%d%d",&v,&c,&l,&r);
        if(c+r<N-10 && (!l || g[l].count(c+r))) {
            int last=g[l][c+r];
            f[i]=f[last]+v; p[i]=last;
            if(r==0 && f[i]>f[sum]) sum=i;
            if(f[i] > f[g[l+c][r]]) g[l+c][r]=i;
        }
    }
    for(; sum; sum=p[sum]) ans[cnt++]=sum;
    printf("%d\n",cnt);
    while(cnt--) printf("%d ",ans[cnt]);
    return 0;
}