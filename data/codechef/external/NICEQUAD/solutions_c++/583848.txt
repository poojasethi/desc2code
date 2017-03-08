#include <stdio.h>
#include <math.h>
#include <limits.h>
#include <memory.h>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define REP(i,a,b) 		for (int i=(a),_b=(b);i<_b;i++)
#define FOR(i,a,b) 		for (int i=(a),_b=(b);i<=_b;i++)
#define DOW(i,a,b) 		for (int i=(a),_b=(b);i>=_b;i--)
#define TR(c,it) 		for (typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define pb 				push_back
#define mp 				make_pair
#define sz(c) 			int((c).size())
#define all(c) 			(c).begin(), (c).end()

typedef long long 		LL;
typedef unsigned long long 	ULL;
typedef pair<int, int> 	ii;
typedef pair<ii, int> 	iii;
typedef vector<int> 	vi;
typedef vector<vi> 		vvi;
typedef vector<string> 	vs;
typedef vector<ii> 	    vii;
typedef vector<vii> 	vvii;

const int MAXN = 30005;

int nTest, n, a[4], x[4], y[4];
LL f[4][2][2], res;

void input() {
    scanf("%d\n", &n);
    memset(f,0,sizeof(f));
    int xx, yy;
    REP(i,0,n) {
        scanf("%d %d\n", &xx, &yy);
        if (xx > 0 && yy > 0) f[0][abs(xx) % 2][abs(yy) % 2] ++;
        if (xx > 0 && yy < 0) f[1][abs(xx) % 2][abs(yy) % 2] ++;
        if (xx < 0 && yy < 0) f[2][abs(xx) % 2][abs(yy) % 2] ++;
        if (xx < 0 && yy > 0) f[3][abs(xx) % 2][abs(yy) % 2] ++;
    }
}

void calc() {
    FOR(i,0,3) {
        x[i] = (a[i] >> 0) & 1;
        y[i] = (a[i] >> 1) & 1;
    }
    
    int cnt = 0;
    FOR(i,0,3) if (abs(x[i] - x[(i + 1) % 4]) % 2 == 1 && abs(y[i] - y[(i + 1) % 4]) % 2 == 1) cnt ++;
    if (cnt % 2 == 1) return;
    
    res += (f[0][x[0]][y[0]] * f[1][x[1]][y[1]] * f[2][x[2]][y[2]] * f[3][x[3]][y[3]]);
}

void attempt(int i) {
    if (i > 3) {
        calc();
        return;
    }
    
    FOR(k,0,3) {
        a[i] = k;
        attempt(i + 1);
    }
}

void process() {
    res = 0;
    attempt(0);
    printf("%lld\n", res);
}

void output() {
}

int main() {
    //freopen("nicequad.inp", "r", stdin);
    //freopen("nicequad.out", "w", stdout);
    
    scanf("%d\n", &nTest);
    REP(i,0,nTest) {
        input();
        process();
        output();
    }

    return 0;
}
