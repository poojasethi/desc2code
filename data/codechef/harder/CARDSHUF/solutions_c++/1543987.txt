#include <map> 
#include <set> 
#include <list>
#include <stack>
#include <cmath> 
#include <queue> 
#include <ctime>
#include <cfloat>
#include <vector> 
#include <string> 
#include <cstdio>
#include <bitset>
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <iomanip>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

#define FILL(X, V) memset((X), (V), sizeof(X))
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())

#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 0; --i)
#define FORIT(i, a) for(TI(a) i = (a).begin(); i != (a).end(); ++i)

#define PB push_back
#define MP make_pair
    
#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL

const double EPS = 1e-9;
inline int SGN(double a) {
    return ((a > EPS)?(1):((a < -EPS)?(-1):(0)));
}
inline int CMP(double a, double b) {
    return SGN(a - b);
}

typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

bool printed;
struct node_t {
	
    int key, pr, sz;
    bool rev;
	node_t *l, *r;
    
	node_t(int k) : key(k), pr(rand()), sz(0), rev(false), l(NULL), r(NULL) {}
    
    /*~node_t(){
		if(l) delete l;
		if(r) delete r;
	}*/	
};

void rotate_right(node_t* &t) {
	node_t *n = t->l;
	t->l = n->r;
	n->r = t;
	t = n;
}

void rotate_left(node_t* &t) {
	node_t *n = t->r;
	t->r = n->l;
	n->l = t;
	t = n;
}

void fix(node_t* t) {
	if(!t) return;    
	t->sz = 1 + ((t->l)?(t->l->sz):(0)) + ((t->r)?(t->r->sz):(0));
}

void push(node_t* t) {
	if(!t) return;    
    
    if (t->rev) {
        t->rev = false;
        swap(t->l, t->r);
        if (t->l) t->l->rev = !(t->l->rev);
        if (t->r) t->r->rev = !(t->r->rev);
    }
}

void insert(node_t* &t, int val, int pos) {
	if (!t) t = new node_t(val);
	else {
		int lsz = ((t->l)?(t->l->sz):(0));
		if (lsz >= pos) insert(t->l, val, pos);
		else insert(t->r, val, pos-lsz-1);
	}
	
	if (t->l && ((t->l->pr) > (t->pr))) rotate_right(t);
	else if (t->r && ((t->r->pr) > (t->pr))) rotate_left(t);
	
	fix(t->l); fix(t->r); fix(t);
}

void merge(node_t* &t, node_t* l, node_t* r) {
    push(l);
    push(r);
    
	if (!l || !r)
		t = l ? l : r;
    else if (l->pr > r->pr)
        merge(l->r, l->r, r), t = l;
    else
        merge(r->l, l, r->l), t = r;
    
	fix(t);
}

void split (node_t* t, node_t* &l, node_t* &r, int pos, int add = 0) {
	if (!t)
		return void (l = r = NULL);
	
    push(t); 
       
    int cur_pos = add + ((t->l)?(t->l->sz):(0));
	if (pos <= cur_pos)
		split(t->l, l, t->l, pos, add), r = t;
	else
		split(t->r, t->r, r, pos, cur_pos+1), l = t;
    
    fix(t);
}

void print(node_t* t) {
    if (!t) return;
    
    push(t);
    print(t->l);
    
    if (printed) cout << " ";
    else printed = true;
    
    cout << t->key;
    
    print(t->r);
}

int main(int argc, char* argv[]) {
	ios::sync_with_stdio(false);
	
    node_t *deck = NULL;
    int N, M;
    cin >> N >> M;
    FOR (i, 1, N) insert(deck,i,i);
	
    int A, B, C;
    node_t *deckA, *deckB, *deckC;
    
    while (M--) {
        cin >> A >> B >> C;
        split(deck, deckA, deck, A);
        split(deck, deckB, deck, B);
        merge(deck,deckA,deck);
        split(deck, deckC, deck, C);
        if (deckB) deckB->rev = !(deckB->rev);
        merge(deck,deckB,deck);
        merge(deck,deckC,deck);        
    }
    
    printed = false;
    print(deck);
    cout << "\n";
    
	return 0;

}
