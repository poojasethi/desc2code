#include <bits/stdc++.h>

using namespace std;

inline void inp(int &n ) {//fast input function
      n=0;
      int ch=getchar(),sign=1;
      while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getchar();}
      while( ch >= '0' && ch <= '9' )
          n=(n<<3)+(n<<1)+ ch-'0', ch=getchar();
      n=n*sign;
}
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
#define N 1005

int D[N];

int main () {
  int n;
  inp(n);

  vector <pii> vec;
  vec.push_back(pii(0,0));

  rep(i,n+1) {
    int x, y;
    inp(x); inp(y);
    vec.push_back(pii(x,y));
  }


  priority_queue<pii,vector<pii>, greater<pii> > Q;
  memset(D, 0x3f, sizeof D);
  Q.push(pii(0,0));
  D[0] = 0;

  while (!Q.empty()){
    int u = Q.top().second;
    int c = Q.top().first;
    Q.pop();
    
    if (D[u] < c) continue;

    if (u == n+1) {
      pi(D[u]); pn;
      break;
    }


    for (int i = 1; i <= n+1; i++) {
      int v = i;
      int weight = (vec[u].first - vec[v].first)*(vec[u].first - vec[v].first) + (vec[u].second - vec[v].second)*(vec[u].second - vec[v].second);
      if (D[v] > D[u] + weight) {
        D[v] = D[u] + weight;
        Q.push(pii(D[v],v));
      }
    }
  }

}