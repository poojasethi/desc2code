#include <bits/stdc++.h>
#define X first
#define Y second
#define INF 1000000009
using namespace std;

typedef pair<int,int> pii;

int n, s, l, a[100005];
int dp[100005];
set <pii> S, R;

int main(){

  scanf("%d %d %d", &n, &s, &l);
  for(int i = 1; i <= n; i ++)
    scanf("%d", &a[i]);

  memset(dp, 0, sizeof dp);
  
  int j = 1;
  for(int i = 1; i <= n; i ++){
    S.insert(pii(a[i], i));
    while(!S.empty() && S.rbegin()->X - S.begin()->X > s){
      S.erase(pii(a[j], j));
      j ++;
    }
    if(i >= l && dp[i - l] != -1)
      R.insert(pii(dp[i - l], i - l));
    while(!R.empty() && R.begin()->Y < j - 1)
      R.erase(R.begin());
    if(R.empty())
      dp[i] = -1;
    else
      dp[i] = R.begin()->X + 1;
  }

  printf("%d\n", dp[n]);

  return 0;
}
