#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1

const int maxn = 200100;
struct Seg{
    ll l,r,h;
    int s;
    Seg(){}
    Seg(ll a,ll b,ll c,int d):l(a),r(b),h(c),s(d){}
    bool operator < (const Seg &a)const{
        return h<a.h;
    }
}ss[maxn<<2];
ll len[maxn<<2];
int cov[maxn<<2];
ll X[maxn];

void PushUp(int rt,int l,int r){
    if(cov[rt]) len[rt]=X[r+1]-X[l];
    else if(l==r) len[rt]=0;
    else len[rt]=len[rt<<1]+len[rt<<1|1];
}
void update(int L,int R,int c,int l,int r,int rt){
    if(L<=l&&r<=R){
        cov[rt]+=c;
        PushUp(rt,l,r);
        return ;
    }
    int m=(l+r)>>1;
    if(L<=m) update(L,R,c,lson);
    if(m<R) update(L,R,c,rson);
    PushUp(rt,l,r);
}

int Bin(ll key,int n,ll X[]){
    int l=0,r=n-1;
    while(l<=r){
        int mid=(r+l)>>1;
        if(X[mid]==key) return mid;
        if(X[mid]<key) l=mid+1;
        else r=mid-1;
    }
    return -1;
}

int main(){
    int n;
    cin>>n;
    int m=0;
    int a,b,c,d;
    for(int i=0;i<n;i++){
        cin>>a>>b>>c>>d;
        if(a>c) swap(a,c);
        if(b>d) swap(b,d);
        ss[m]=Seg(a-1,c,b-1,1);
        X[m++]=a-1;
        ss[m]=Seg(a-1,c,d,-1);
        X[m++]=c;
    }
    sort(ss,ss+m);
    sort(X,X+m);
    int k=1;
    for(int i=1;i<m;i++)
        if(X[i]!=X[i-1])
            X[k++]=X[i];
    ll ret=0;
    memset(cov,0,sizeof(cov));
    memset(len,0,sizeof(len));
    for(int i=0;i<m-1;i++){
        int l=Bin(ss[i].l,k,X);
        int r=Bin(ss[i].r,k,X)-1;
        if(l<=r) update(l,r,ss[i].s,0,k-1,1);
        ret+=len[1]*(ss[i+1].h-ss[i].h);
    }
    cout<<ret<<endl;
    return 0;
}
