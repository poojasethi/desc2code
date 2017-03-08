#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
#include <functional>
using namespace std;

#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define ll long long
#define ld long double
#define mod 1000000007
#define inf 1061109567LL
#define pii pair< int, int >
#define pll pair< ll, ll >
#define psi pair< string, int >
#define BLOCK 250
#define gc getchar_unlocked
inline void sc(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
#define N 100001
#define maxval 1000001
struct node {
	int L, R, i;
}q[N];
int a[N];
int answer;
vector <int> cnt[1000001];
int l[1000001];
int r[1000001];
int ans[N];
int s[N+1];
int bit[8*1000000];
inline bool cmp(node x, node y) {
	if(x.L/BLOCK != y.L/BLOCK) {
		return x.L/BLOCK < y.L/BLOCK;
	}
	return x.R < y.R;
}
inline void update(int i,int lt,int rt,int idx,int val){
	if(lt==rt){
		bit[i] = val;
		//cout<<lt<<endl;
		return;
	}
	if(idx<=(lt+rt)/2)update(2*i,lt,(lt+rt)/2,idx,val);
	else update(2*i+1,1+(lt+rt)/2,rt,idx,val);
	bit[i] = max(bit[i*2],bit[2*i+1]);
}

inline void add(int val,int f) {
	if(f){
		r[val]++;
		if(l[val]==-1)
			l[val]++;
	}
	else{
		l[val]--;
	}
	//cout<<val<<" "<<l[val]<<" "<<r[val]<<" "<<cnt[val][r[val]]-cnt[val][l[val]]<<endl;
	update(1,0,maxval,val,cnt[val][r[val]] - cnt[val][l[val]]);
}

inline void remove(int val,int f) {
	if(l[val]>r[val])
		return ;
	if(!f){
		l[val]++;
	}
	else{
		r[val]--;
	}
	if(l[val]>r[val])
		return ;
	//cout<<"asdf "<<val<<" "<<l[val]<<" "<<r[val]<<" "<<cnt[val][r[val]]<<" "<<cnt[val][l[val]]<<endl;
	update(1,0,maxval,val,cnt[val][r[val]] - cnt[val][l[val]]);
}

int main() {
	int n,m,k;
	sc(n);sc(m);sc(k);
	for(int i=0; i<n; i++)
		sc(a[i]);
	s[0]=0;
	cnt[s[0]].PB(0);
	for(int i=1;i<=n;i++){
		s[i]=(a[i-1]+s[i-1])%k;
		cnt[s[i]].PB(i);
		//cout<<s[i]<<" ";
	}
	//cout<<endl;
	for(int i=0;i<maxval;i++){
		l[i]=r[i]=-1;
	}
	//l[N]=r[N]=0;

	for(int i=0; i<m; i++) {
		scanf("%d%d", &q[i].L, &q[i].R);
		q[i].L--;// q[i].R--;
		q[i].i = i;
	}

	sort(q, q + m, cmp);

	int currentL = 0, currentR = 0;
	for(int i=0; i<m; i++) {
		int L = q[i].L, R = q[i].R;
		while(currentR <= R) {
			add(s[currentR],1);
			currentR++;
		}
		while(currentR > R+1) {
			remove(s[currentR-1],1);
			currentR--;
		}
		while(currentL > L) {
			add(s[currentL-1],0);
			currentL--;
		}
		while(currentL < L) {
			remove(s[currentL],0);
			//cout<<s[currentL]<<endl;
			currentL++;
		}
		ans[q[i].i] = bit[1];
		//cout<<bit[1]<<endl;
	}

	for(int i=0; i<m; i++)
		printf("%d\n", ans[i]);
}
