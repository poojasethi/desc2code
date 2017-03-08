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
#define N 4000005

char str[N];

int main () {
  

  while (scanf("%s",str) == 1 && str[0] != 'E') {
    int n = strlen(str);
    int lps[n];
    memset(lps,0,sizeof(lps));
    int len = 0;
    
    fu(i,1,n-1){
      while (1) {
        if (str[i] == str[len]) {
          len++;
          lps[i] = len;
          break;  
        }
        if (len == 0) {
          lps[i] = 0;
          break;
        }
        len = lps[len-1];
      }
    }
    rep(i,n-1) {
      pi(lps[i]); ps;
    }
    pi(lps[n-1]); pn;
  }
}