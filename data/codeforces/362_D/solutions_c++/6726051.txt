#include<queue>
#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const int maxn=110000;
int n,m,p,q;
int fa[maxn];
long long s[maxn];
struct cmp{
    bool operator()(int &a,int &b){ 
        return s[a]>s[b];
    }
};
void read(int &x){
    char ch;
    x=0;
    while (ch=getchar(),ch==' '||ch=='\n');
    while (isdigit(ch)){
        x=x*10+ch-'0';
        ch=getchar();
    }
}
int find(int i){
    if ( fa[i]!=i) fa[i]=find(fa[i]);
    return fa[i];
}
void init(){
    read(n),read(m),read(p),read(q);
    q=n-q;
    for (int i=1;i<=n;++i) fa[i]=i;
    int a,b,d,x,y;
    for (int i=1;i<=m;++i){
        read(a),read(b),read(d);
        int x=find(a),y=find(b);
        if (x!=y){
            q--;
            s[x]+=s[y]+d;
            fa[y]=x;
        } else s[x]+=d;
    }
}
void work(){
    if (q<0||q>p||!q&&!m&&p){
        puts("NO");
        return;
    }
    puts("YES");
    priority_queue<int,vector<int>,cmp> Q;
    for (int i=1;i<=n;++i)
        if (find(i)==i) Q.push(i);
    int x,y;
    while (q--){
        x=Q.top(),Q.pop();
        y=Q.top(),Q.pop();
        printf("%d %d\n",x,y);
        s[x]+=s[y];
        s[x]+=min((long long)1e9,s[x]+1);
        fa[y]=x;
        Q.push(x);
        p--;
    }
    for (int i=1;i<=n;++i)
        if (find(i)!=i){
            for (int j=1;j<=p;++j)
                printf("%d %d\n",find(i),i);
            break;
        }
}

int main(){
    init();
    work();
    return 0;
}