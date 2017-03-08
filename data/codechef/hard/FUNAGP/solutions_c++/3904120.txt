/*
user  : triveni
date  : 05/05/2014
time  : 15:26:11
*/
#include <bits/stdc++.h>

using namespace std;

#define      pii               std::pair<int,int>
#define      mp(a,b)           std::make_pair(a,b)
#define      X                 first
#define      Y                 second

typedef long long ll;
ll p, p1, p2, R, N, A[3][100002];	// 0: R^i, 1: sigma(R^i) , 2: sigma(iR^i)
int H, low, high;

ll pow_mod(ll a, ll b)
{
    ll ans = 1;
    while(b)
    {
        if(b&1) ans = ans * a % p2;
        b >>= 1;
        a = a * a % p2;
    }
    return ans;
}

ll mod(ll a, ll b)
{
    a %= p;
    b %= p;
    long double res = a;
    res *= b;
    ll c = ll(res/p);
    a *= b;
    a -= c*p;
    a %= p;
    if(a<0) a += p;
    return a;
}

ll get_sum(ll S, ll D, int n)
{
    return (mod(S,A[1][n-1]) + mod(D,A[2][n-1]))%p;
}
struct node
{
    int sz;
    long long sum, S, D;
    void merge(node& l, node& r)
    {
        sum = (l.sum + r.sum)%p;
        sz = l.sz + r.sz;
        S = D = 0;
    }
    void split(node& l, node& r)
    {
        ll s_ = mod(((S + mod(l.sz, D))%p), A[0][l.sz]), d_ = mod(D,A[0][l.sz]);
        l.S = (l.S + S)%p, r.S = (r.S + s_);
        l.D = (l.D + D)%p, r.D = (r.D + d_);
        l.sum = (l.sum + get_sum(S,D,l.sz))%p, r.sum = (r.sum + get_sum(s_,d_,r.sz));
        S = D = 0; // optional
    }
    void update(ll& s, ll& d)
    {
        S = (S + s)%p, D = (D + d)%p;
        sum = (sum + get_sum(s,d,sz))%p;
        s = mod(((s + mod(sz,d))%p), A[0][sz]), d = mod(d, A[0][sz]);
        return ;
    }
    void pt_update(int g)
    {
        sum = sum%p2;
        sum = pow_mod(sum,g);
    }
} Tree[262144];	// [low, high]

void mergeup(int root)
{
    if(root >= low) return;
    mergeup(root*2);
    mergeup(root*2+1);
    Tree[root].merge(Tree[root*2], Tree[root*2+1]);
}
void build_segtree(int Ar[])
{
    H = ceil(log2(N));
    low = 1<<H;
    high = low * 2 - 1;
    for(int i=0; i<N; ++i)
    {
        Tree[i+low] = (node)
        {
            1,Ar[i],0,Ar[i]
        }; // 4th argument could be 0
    }
    for(int i=low+N; i<=high; ++i)
    {
        Tree[i] = (node)
        {
            0,0,0,0
        };
    }
    mergeup(1);
}

void init()
{
    if(p1 != p2) p = p1*p2;
    else p = p1;
    A[0][0] = A[1][0] = 1, A[2][0] = 0;
    for(ll i = 1; i<=N; ++i)
    {
        A[0][i] = mod(A[0][i-1],R);
        A[1][i] = (A[1][i-1] + A[0][i])%p;
        A[2][i] = (A[2][i-1] + mod(A[0][i],i))%p;
    }
    return ;
}

void point_update(int idx, int L, int RR, int i, ll g)
{
    if(L==RR)
    {
        Tree[idx].pt_update(g);
        return ;
    }
    int left = idx<<1, right = left|1, mid = (L+RR)>>1;
    Tree[idx].split(Tree[left], Tree[right]);
    if(mid>=i) point_update(left, L, mid, i, g);
    else  point_update(right, mid+1, RR, i, g);
    Tree[idx].merge(Tree[left], Tree[right]);
    return ;
}
void update(int idx, int L, int RR, int i, int j, ll& S, ll& D)
{
    if(i<=L && j>=RR)
    {
        Tree[idx].update(S,D);
        return ;
    }
    int left = idx<<1, right = left|1, mid = (L+RR)>>1;
    Tree[idx].split(Tree[left], Tree[right]);
    if(mid>=i) update(left, L, mid, i, j, S, D);
    if(mid<j)  update(right, mid+1, RR, i, j, S, D);
    Tree[idx].merge(Tree[left], Tree[right]);

    return ;
}
ll query(int idx, int L, int RR, int i, int j)
{
    if(i<=L && j>=RR)
        return Tree[idx].sum;

    int left = idx<<1, right = left|1, mid = (L+RR)>>1;
    Tree[idx].split(Tree[left], Tree[right]);
    ll ans1 = 0, ans2 = 0;
    if(mid>=i) ans1 = query(left, L, mid, i, j);
    if(mid<j)  ans2 = query(right, mid+1, RR, i, j);
    Tree[idx].merge(Tree[left], Tree[right]);
    return (ans1+ans2)%p;
}
void solve()
{

    int Q, temp[100001];
    scanf("%lld%d%lld%lld%lld",&N,&Q,&R,&p1,&p2);
    for(int i=0; i<N; ++i)
        scanf("%d",temp+i);
    init();
    build_segtree(temp);
    while(Q--)
    {
        int cas;
        scanf("%d",&cas);
        if(cas ==0)
        {
            ll ss, dd, xxx, yy;
            scanf("%lld%lld%lld%lld",&ss,&dd,&xxx,&yy);
            xxx--, yy--;
            update(1,low, high, low+xxx, low+yy, ss, dd);
        }
        else if(cas == 1)
        {
            ll xxx, g;
            scanf("%lld%lld",&xxx,&g);
            point_update(1, low, high, low+xxx-1, g);
        }
        else if(cas==2)
        {
            int lll, rr;
            scanf("%d%d",&lll,&rr);
            lll--, rr--;
            ll aaa = query(1,low,high,lll+low,rr+low);
            printf("%lld\n",aaa%p1);
        }
    }
}

int main()
{
//    freopen("1.txt","r",stdin);
    int T;
    scanf("%d",&T);
    while(T--)
    {
        solve();
    }
    return 0;
}
