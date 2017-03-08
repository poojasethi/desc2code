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

typedef unsigned long long llu;

vector <int> bin;
int digit;
llu dp[20][2][2][2];


void createBinary (llu n) {
  while (n > 0) {
    bin.push_back(n%10);
    n /= 10;
  }
  bin.push_back(0);
  reverse(bin.begin(), bin.end());
}

llu gcd(llu a, llu b) {
  if (b == 0)
    return a;
  return gcd (b, a % b);
}

llu find (int index, int less, int present, int started) {
  llu ans = dp[index][less][present][started];

  if (ans != -1) return ans;
  
  if (index == bin.size()) {
    if (present > 0 && started > 0) ans = 1;
    else ans = 0;
  }
  else {
    ans = 0;
    for (int i = 0; i <= 9; i++) {
      if (less > 0 && i > bin[index]) continue;  
      
      int nindex = index + 1;
      int nless = 0;

      if (less == 1){
        if (i == bin[index]) nless = 1;
      }

      int nstarted = 0;
      if (started > 0) nstarted = 1;
      else if (i != 0) nstarted = 1;

      int npresent = 0;

      if (nstarted > 0 && i == digit) {
        npresent = 1;
      }
      if (present > 0) npresent = 1;

      ans += find(nindex, nless, npresent, nstarted);
    }
  }

  dp[index][less][present][started] = ans;
  return ans;

}

int main () {
  int t;
  inp(t);

  while (t--) {
    bin.clear();
    llu n;
    scanf("%llu",&n);
    createBinary(n);
    llu num = 0;
    for (digit = 0; digit <= 9; digit++) {
      memset(dp,-1,sizeof(dp));
      num += find(0,1,0,0);
    }

    llu den = 10*n;

    llu fact = gcd(num,den);
    num /= fact;
    den /= fact;
    printf("%lli/%lli\n",num,den);
  }
}