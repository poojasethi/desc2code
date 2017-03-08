#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <bitset>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int X,Y;
char board[510][510];
int x3[600010],y3[600010],x2[600010],y2[600010];
bool ans[600010];

bitset <510> dp1[510][510], dp2[510][510];

void dfs(int L, int R, vector <int> q){
    int i,j;
    int M = (L + R) / 2;
    
    for(i=L;i<=M;i++) REP(j,Y) dp1[i][j].reset();
    for(i=M;i<=R;i++) REP(j,Y) dp2[i][j].reset();
    
    for(i=M;i>=L;i--) for(j=Y-1;j>=0;j--) if(board[i][j] == '.'){
        if(i == M) dp1[i][j].set(j);
        if(i+1 <= M) dp1[i][j] |= dp1[i+1][j];
        if(j+1 < Y) dp1[i][j] |= dp1[i][j+1]; 
    }
    
    for(i=M;i<=R;i++) REP(j,Y) if(board[i][j] == '.'){
        if(i == M) dp2[i][j].set(j);
        if(i-1 >= M) dp2[i][j] |= dp2[i-1][j];
        if(j-1 >= 0) dp2[i][j] |= dp2[i][j-1];
    }
    
    REP(i,q.size()){
        int id = q[i];
        if(x3[id] <= M && x2[id] >= M && (dp1[x3[id]][y3[id]] & dp2[x2[id]][y2[id]]).any()) ans[id] = true;
    }
    
    if(L < M){
        vector <int> q2;
        REP(i,q.size()) if(x2[q[i]] < M) q2.push_back(q[i]);
        dfs(L, M, q2);
    }
    
    if(M+1 < R){
        vector <int> q2;
        REP(i,q.size()) if(x3[q[i]] > M) q2.push_back(q[i]);
        dfs(M+1, R, q2);
    }
}

int main(void){
    int Q,i;
    
    scanf("%d%d", &X, &Y);
    REP(i,X) scanf("%s", board[i]);
    scanf("%d", &Q);
    REP(i,Q) scanf("%d%d%d%d", &x3[i], &y3[i], &x2[i], &y2[i]);
    REP(i,Q) {x3[i]--; y3[i]--; x2[i]--; y2[i]--;}
    
    vector <int> q;
    REP(i,Q) q.push_back(i);
    dfs(0, X, q);
    
    REP(i,Q) if(ans[i]) printf("Yes\n"); else printf("No\n");
    
    return 0;
}
