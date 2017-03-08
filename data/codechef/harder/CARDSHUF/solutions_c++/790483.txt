#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <climits>
//#include <ext/hash_map>
#include<tr1/random>



using namespace std;
using namespace __gnu_cxx;



#define REP(i,n) for(int i = 0; i < int(n); ++i)
#define REPV(i, n) for (int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)

#define FE(i,t) for (__typeof((t).begin())i=(t).begin();i!=(t).end();++i)
#define FEV(i,t) for (__typeof((t).rbegin())i=(t).rbegin();i!=(t).rend();++i)

#define two(x) (1LL << (x))
#define ALL(a) (a).begin(), (a).end()


#define pb push_back
#define ST first
#define ND second
#define MP(x,y) make_pair(x, y)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T> void checkmin(T &a, T b){if (b<a)a=b;}
template<class T> void checkmax(T &a, T b){if (b>a)a=b;}
template<class T> void out(T t[], int n){REP(i, n)cout<<t[i]<<" "; cout<<endl;}
template<class T> void out(vector<T> t, int n=-1){for (int i=0; i<(n==-1?t.size():n); ++i) cout<<t[i]<<" "; cout<<endl;}
inline int count_bit(int n){return (n==0)?0:1+count_bit(n&(n-1));}
inline int low_bit(int n){return (n^n-1)&n;}
inline int ctz(int n){return (n==0?-1:ctz(n>>1)+1);}
int toInt(string s){int a; istringstream(s)>>a; return a;}
string toStr(int a){ostringstream os; os<<a; return os.str();}


const int maxn=111111;

struct node{
    node():l(0),r(0),cnt(1),f(0){}
    node *l, *r;
    int v, cnt;
    int w; int f;
};

node nl[maxn];
int pos;


void norm(node *x){
    if (x->f){
        x->f=0, swap(x->l, x->r);
        if (x->l) x->l->f^=1;
        if (x->r) x->r->f^=1; 
    }
}
void disp(node *x){
    if (!x) return;
    norm(x);
    disp(x->l); printf("%d ", x->v+1); disp(x->r);
}

int count(node *x){return x?x->cnt:0;}

void split(node *p, node *&A, node *&B, int cnt){
    if (!p){A=B=0; return;}

    norm(p);
    if (cnt<=count(p->l)){
        node *u;
        split(p->l, A, u, cnt);
        p->l=u;
        B=p;
        p->cnt-=count(A);
    }else{
        node *u;
        split(p->r, u, B, cnt-count(p->l)-1);
        p->cnt-=count(B);
        p->r=u;
        A=p;
    }
}


node *merge(node *root, node *a){
    if (!root) return a;
    if (!a) return root;
    norm(root); norm(a);

    if (root->w>=a->w){
        root->cnt+=count(a);
        root->l=merge(root->l, a);
        return root;
    }else{
        a->cnt+=count(root);
        a->r=merge(root, a->r);
        return a;
    }
}



int main(){
    int n, m;
    cin>>n>>m;
    tr1::mt19937 prng;
    prng.seed(316);
    pos=0;
    node *root=nl;
    root->v=0;
    REP(i,n-1){
        node *a=nl+i+1;
        a->v=i+1;
        a->w=prng();
        root=merge(a, root);
    }
    REP(i, m){
        int a, b, c;
        scanf(" %d %d %d", &a, &b, &c);

        node *an, *bn;
        an=bn=0;
        split(root, an, root, a);
        split(root, bn, root, b);
        if (bn) bn->f^=1;

        root=merge(root, an);
        an=0;
        split(root, an, root, c);
        root=merge(root, bn);
        root=merge(root, an);
    }
    disp(root); printf("\n");
    return 0;
}

