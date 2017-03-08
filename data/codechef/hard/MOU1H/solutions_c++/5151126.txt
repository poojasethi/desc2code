//Template
 
// By Anudeep :)
//Includes
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
 
//M lazy ;)
typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)
 
#define gi(n) scanf("%d",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) printf("%lld",n)
#define ps printf(" ")
#define pn printf("\n")
#define N 222222
 
struct node { int x,y,i; };
int a[N],n,p[N][20];
node l[N];
ll ans;
 
bool cmp(node a, node b) {
  return (a.x<b.x) || (a.x==b.x && a.y<b.y);
}
 
void construct() {
  memset(p, -1, sizeof p);
  int cur=1,step=0;
  rep(i,n) l[i].x=a[i],l[i].y=-1,l[i].i=i;
  while(1) {
    sort(l,l+n,cmp);
    rep(i,n) p[l[i].i][step] = (i>0 && l[i].x==l[i-1].x && l[i].y==l[i-1].y)?p[l[i-1].i][step]:i;
    step++;
    // rep(i,n) { pi(p[i][step-1]); ps; } pn;
    if(cur > n) break;
    rep(i,n) {
      l[i].x = p[i][step-1];
      l[i].y = i+cur<n? p[i+cur][step-1]: -1;
      l[i].i = i;
    }
    cur <<= 1;
  }
  // rep(i,n) { pi(p[i][step-1]); ps; } pn;
}
 
int count(int x,int y) {
  int k=0;
  fd(i,19,0) if(p[x][i]!=-1 && p[x][i]==p[y][i]) x+=(1<<i),y+=(1<<i),k+=(1<<i);
  return k;
}
 
void solve() {
  construct();
  ans = 0;
  fu(i,1,n-1) ans += count(l[i].i, l[i-1].i);
  ans = ll(n)*(n+1)/2 - ans;
  pl(ans%1000000009); pn;
}
 
int main() {
  int t,prev,cur;
  gi(t);
  while(t--) {
    gi(n);
    gi(prev);
    n--;
    rep(i,n) {
      gi(cur);
      a[i] = cur-prev;
      prev=cur;
    }
    solve();
  }
} 