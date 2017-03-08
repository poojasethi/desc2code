#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)

const int N=101000;
map<int,int> hs;

int n,a,b,f[N],vs[N],sta[N],p[N];
int find(int x) { return f[x]==x?x:f[x]=find(f[x]);}
int main() {
    scanf("%d%d%d",&n,&a,&b);
    rep(i,1,n+1) scanf("%d",p+i),hs[p[i]]=i,f[i]=i;
    rep(i,1,n+1) {
        if (hs.count(a-p[i])) f[find(hs[a-p[i]])]=find(i),vs[i]|=1;
        if (hs.count(b-p[i])) f[find(hs[b-p[i]])]=find(i),vs[i]|=2;
    }
    rep(i,1,n+1) sta[i]=3;
    rep(i,1,n+1) sta[find(i)]&=vs[i];
    rep(i,1,n+1) if (sta[i]==0) {
        puts("NO"); return 0;
    }
    puts("YES");
    rep(i,1,n+1) {
        int st=sta[find(i)];
        putchar('0'+((st&1)==0));
        if (i!=n) putchar(' ');
    }
    puts("");
}