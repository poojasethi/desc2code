#include <iostream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <vector>

using namespace std;
const int maxn = 1e5+100;

typedef unsigned long long ULL;

ULL p[10000],a[10000];
int Next[10000];

ULL ans,n;

set<int> S;

bool chk(int x)
{
  while(x)
  {
    int dig = x%10;
    if(dig != 4 && dig != 7) return false;
    x /= 10;
  }
  return true;
}

int main()
{
  int num,i,j,m = 0, k;
  set<int>::iterator iter1,iter2;
  cin>>n;
  for(i=1;i<=n;i++)
  {
    scanf("%d",&num);
    if(chk(num))
    {
      p[++m] = i;
      a[m] = num;
    }
  }

  for(i=1;i<=m;i++){
    for(j=i+1;j<=m;j++){
      if(a[i]==a[j]) break;
    }
    Next[i] = j;
  }
  p[m+1] = n+1;
  ans = n*(n-1)/2 + n*(n-1)*(n-2)/3 + n*(n-1)/2*(n-2)/3*(n-3)/4;

  for(i=1;i<=m;i++)
  {
    S.clear(); ULL tmp = 0;
    S.insert(i); S.insert(m+1);

    for(j=i;j>=1;j--)
    {
      if(Next[j]>i)
	for(k=Next[j];k<=m;k = Next[k])
	{
	  iter1 = iter2 = S.insert(k).first;
	  iter1--, iter2++;
	  if(*iter1>i)
	    tmp += (ULL)(p[*iter2] - p[k])*(p[k] - p[*iter1])*(p[i+1] -p[i]);
	  else
	  {
	    tmp += (ULL)(p[k] - p[i]+1)*(p[k]-p[i])/2*(p[*iter2] - p[k]);
	    tmp -= (ULL)(p[k] - p[i+1]+1)*(p[k]-p[i+1])/2*(p[*iter2] - p[k]);
	  }
	}
      ans -= (ULL)(p[j]-p[j-1])*tmp;
    }
  }
  cout<<ans<<endl;
}