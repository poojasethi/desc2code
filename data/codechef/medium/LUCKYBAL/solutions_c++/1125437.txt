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

int main(){
    int test;
    char s[100001];
    scanf("%d\n",&test);
    REP(i,test){
        gets(s);
        int i=0,j=0,n=strlen(s);
        ll res=ll(n)*(n+1)/2;
        while(i<n){
            while(i<n && s[i]!='7') i++;
            if(i==n) break;
            j=i;
            while(j<n && s[j]=='7') j++;
            res-=ll(j-i)*(j-i+1)/2;
            i=j;
        }
        cout<<res<<endl;
    }
    return 0;
}
