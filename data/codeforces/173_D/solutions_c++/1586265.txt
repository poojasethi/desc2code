#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

#define rep(i,n) for(int i=0; i<n; i++)
#define reps(i,m,n) for(int i=m; i<n; i++)
#define repe(i,m,n) for(int i=m; i<=n; i++)
#define repi(it,stl) for(typeof((stl).begin()) it = (stl).begin(); (it)!=stl.end(); ++(it))
#define sz(a) ((int)(a).size())
#define mem(a,n) memset((a), (n), sizeof(a))
#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define vi vector<int>
#define vs vector<string>
#define sstr stringstream 
#define fnd(v,x) (find(all((v)),(x))!=(v).end())
#define itr(A,B) typeof(B) A = B
typedef long long ll;
using namespace std;

const int size = 100002;
vi g[size];
vi side[2];
bool vis[size];
bool inside[size];
int mark[size];
void visit(int idx, bool s){
    side[s].push_back(idx);
    inside[idx]=s;
    rep(i,sz(g[idx])){
        int nxt = g[idx][i];
        if(vis[nxt]) continue;
        vis[nxt] = 1;
        visit(nxt,!s);
    }
}

int group=1;
bool isValid(){
    int valid=-1;
    for (int i= 0; i< side[0].size(); ++i) {
        int nxt = side[0][i];
        if(!mark[nxt] && g[nxt].size() < side[1].size()-1){
            valid = nxt;
            break;
        }
    }
    if(valid==-1)
        return 0;

    mark[valid] = group;
    mem(vis,0);
    rep(j,g[valid].size()){
        int nxt = g[valid][j];
        vis[nxt]=1;
    }
    int cnt=0;
    rep(j,sz(side[1])){
        if(cnt == 2) break;
        if(!vis[side[1][j]])
            ++cnt, mark[side[1][j]]=group;
    }
    group++;
    return 1;
}


int main(){
#ifndef ONLINE_JUDGE
    freopen("in","rt",stdin);
    freopen("out","wt",stdout);
#endif

    int n,m,a,b;
    scanf("%d%d",&n,&m);
    rep(i,m){
        scanf("%d%d",&a,&b);
        --a,--b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    rep(i,n) if(!vis[i])
            vis[i]=1, visit(i,0);

    if((side[0].size()+side[1].size())%3){
        printf("NO");
        return 0;
    }
    if(sz(side[0])%3 == 2) swap(side[0],side[1]);

    if(sz(side[0])%3 == 1){
        if(isValid()) goto yes;
        swap(side[0],side[1]);
        if(!isValid() || !isValid()){
            printf("NO\n");
            return 0;
        }
    }

yes:
    int cnt=0;
    rep(k,2){
        repi(i,side[k]){
            if(mark[*i]) continue;
            if(cnt == 3)
                cnt = 0,++group;
            mark[*i]=group;
            ++cnt;
        }
    }
    printf("YES\n");
    rep(i,n)    printf("%d ",mark[i]);
    return 0;

}





