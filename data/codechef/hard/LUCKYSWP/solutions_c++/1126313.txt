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

#define maxn 100007

char s[maxn];
int n, test, t,s4[maxn],s7[maxn],max4[maxn];

//#include <conio.h>
int main(){
    //freopen("test.txt","r",stdin);
    scanf("%d\n", &test);
    REP(index,test){
        reset(s4,0); reset(s7,0); reset(max4,0);
        scanf("%s\n",&s);
        n=strlen(s);
        REP(i,n) s4[i]=((i>0)?s4[i-1]:0) + (s[i]=='4');
        REPD(i,n) s7[i]=((i<n-1)?s7[i+1]:0) + (s[i]=='7');
        t=0;
        REPD(i,n){
            if(s[i]=='4') t++; else t--;
            t=max(t,0);
            max4[i]=max(t,(i<n-1)?max4[i+1]:0);
        }
        int res=s7[0]+max4[0];
        REP(i,n) res=max(res,s4[i]+s7[i+1]+max4[i+1]);
        printf("%d\n",res);
    }
    //getch();
    return 0;
}
        
