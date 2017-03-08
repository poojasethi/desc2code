// written by lonerdude(dvdreddy)
// all rights reserved
//the template by dvdreddy
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define s(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sf(x) scanf("%lf",&x)
#define ss(x) scanf("%s",&x)

#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,n)  f(i,0,n)

typedef long long ll;

int maxs = 10000000;

ll mod = 10000;

int res[10000005];
ll dp[102000];

void init(){  
  res[0] = 1;
  dp[0] = 1;
  int cur_max = 1;
  ll x, ax;
  int lenx;
  int cnt = 0;
  ll* temp;
  f (i, 1, maxs + 1){
    x = ((ll) ((i % mod) + 1)) * ((ll) ((i % mod) + 1));
    ax  = (x % mod);
    temp = lower_bound(dp, dp + cur_max, ax);
    int lenx = temp - dp;
    if (lenx ==  cur_max){
      cur_max++;
      *temp = ax;
      if (cur_max == 1044){
	f (j, i, maxs + 1){
	  res[j] = cur_max;
	}
	break;
      }
    } else if (*temp > ax){
      *temp = ax;
    }
    res[i] = cur_max;
  }
}

int main(){
  int n; int k;
  int t;
  init();
  s(t);
  while (t--){
    s(n); s(k);
    if (res[n - 1] < k){
      cout << "0" << endl;
    } else {
      cout << "1" << endl;
    }
  }
}
