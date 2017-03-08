#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn = 100007;

struct node{
    int c,v;
    node *next[2];
}*root;

int a[maxn],n,k;
int tmp[maxn*5];
int cnt;
vector<int> res;
vector<node*> lst[31];

node *newnode(int v){
    node *p = new node;
    p->c = 0;
    p->v = v;
    p->next[0] = p->next[1] = NULL;
    return p;
}

void dfs(node *p, int val){
    if(!p->next[0] && !p->next[1]){
        for(int j=0; j < p->c; ++j) tmp[++cnt]=val;
        return;
    }
    if(p->next[0]) dfs(p->next[0], val<<1);
    if(p->next[1]) dfs(p->next[1], (val<<1) | 1);
}

int main(){
//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
    scanf("%d%d",&n,&k);
    root = newnode(0);
//    n=100000; k=250000;
    for(int idx=1,v; idx<=n; ++idx){
        scanf("%d",&v);
        a[idx] = v;
        node *p = root;
        int depth = 0;
        int val=0;
        for(int i=30; i>=0; --i){
            int b=v>>i&1;
            if(b) val |= 1<<i;
            if(!p->next[b]){
                p->next[b] = newnode(val);
                lst[depth].pb(p->next[b]);
            }
            p->c++;
            p=p->next[b];
            ++depth;
        }
        p->c++;
    }

    for(int i=30; i>=0; --i){
        ll sum = 0;
        for(int j=0; j<sz(lst[i]); ++j){
            node *p=lst[i][j];
            sum += (p->c)*(p->c-1)/2;
            if(sum>=k) break;
        }
        if(sum>=k){
            if(i==30){
                for(int i=0; i<k; ++i) printf("0 ");
                return 0;
            }
            for(int j=0; j<sz(lst[i]); ++j){
                node *p = lst[i][j];
                cnt=0;
                dfs(p, p->v);
                for(int x=1; x<cnt; ++x)
                    for(int y=x+1; y<=cnt; ++y)
                        res.pb(tmp[x]^tmp[y]);
            }
            sort(res.begin(), res.end());
            for(int i=0; i<k; ++i){
                printf("%d ",res[i]);
            }
            return 0;
        }
    }

}
