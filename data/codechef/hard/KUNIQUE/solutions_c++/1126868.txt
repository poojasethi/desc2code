#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#define FOR(a,b,c) for (int a=b;a<=c;a++)
#define FORD(a,b,c) for (int a=b;a>=c;a--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define REPD(i,a) for(int i=(a)-1; i>=0; --i)
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii,int> iii;

#define maxn 50007

int n,k;
map<int,int> mymap;
set<pii> set1;
set<int> v;

void solve(){
    scanf("%d%d",&n,&k);
    mymap.clear();
    int t;
    FOR(i,1,n){
        scanf("%d",&t);
        if(mymap.find(t)!=mymap.end()) mymap[t]++; else mymap[t]=1;
    }
    set1.clear();
    for(map<int,int>::iterator it=mymap.begin(); it!=mymap.end(); it++){
        if(it->se>n/k){printf("-1\n"); return;}
        set1.insert(pii(it->se,it->fi));
    }
    FORD(i,n/k,1){
        v.clear();
        for(set<pii>::reverse_iterator it=set1.rbegin(); it!=set1.rend() && it->fi >= i; it++) v.insert(it->se);
        for(map<int,int>::iterator it=mymap.begin(); it!=mymap.end() && sz(v)<k; it++) if(v.find(it->fi)==v.end()) v.insert(it->fi);
        for(set<int>::iterator it=v.begin(); it!=v.end(); it++){
            printf("%d ",*it);
            t=mymap[*it];
            set1.erase(set1.find(pii(t,*it)));
            mymap[*it]--;
            if(t>1) set1.insert(pii(t-1,*it)); else mymap.erase(*it);
        }
    }
    printf("\n");
}    
//#include <conio.h>
int main(){
    //freopen("test.txt","r",stdin);
    int T;
    scanf("%d",&T);
    REP(i,T) 
    solve();
    //getch();
    return 0;
}
