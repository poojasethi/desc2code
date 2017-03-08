#include <vector>
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

typedef long long ll;

int M;
char strC[32];
ll n, P, F;
int Cint, Cdouble;
const int d9 = 1000000000;


void solve0()
{
  if(Cint >= 2)
    {
      F = n - 1;
      P = 2 * (n - 1) * (n - 1);
    }
  else 
    {
      F = (n * (n - 1)) / 2;
      P = n * (n - 1);
    }
}

void solve1()
{
  solve0();
  F--;
}

void solve2_CommonVertex()
{
  solve0();
  F -= 2;
}

void solve2_DistinctVertex()
{
  if(Cint >= 2 * (n - 2))
    {
      F = n - 3;
      ll d1, d3, d4, rest;
      
      d1 = n;

      d3 = 2 + 2 * (n - 3);

      d4 = 1 + 2 + 3 * (n - 3);
      
      rest = (n - 3) * (1 + 2 * (n - 3) + 3);
      
      P = d1 + d3 + d4 + rest;
    }
  else if(Cint >= 2)
    {
      F = n - 2;
      ll d1, d34, rest;
      
      d1 = n - 1;
      
      d34 = 2 * (2 + 2 * (n - 3));
      
      rest = (n - 3) * (1 + 2 * (n - 2));
      
      P = rest + d34 + d1;
    }
  else
    {
      solve0();
      F -= 2;
    }
}

void processC()
{
    Cint=0;
    Cdouble=0;
  
    int len=strlen(strC),i,d;
    for(i=0;i<len;i++)
    {
        if(strC[i]=='.')
            break;
        Cint*=10;
        Cint+=strC[i]-'0';
    }
    i++;
    for(d=0;i<len;i++,d++)
    {
        Cdouble*=10;
        Cdouble+=strC[i]-'0';
    }
    for(;d<9;d++)
    {
        Cdouble*=10;
    }
}

void calcAns()
{
  ll Aint, Adouble, Fint, Fdouble;
  Fint = F / d9;
  Fdouble = F % d9;
  //(Cint + Cdouble * 10(-9)) * (Fint * 10(9) + Fdouble)
  cerr << P << " " << F << endl;
  Aint = P + Cint * F + Fint * Cdouble + (Cdouble * Fdouble) / d9;
  Adouble = (Cdouble * Fdouble) % d9;
  printf("%lld.%09lld\n", Aint, Adouble);
}

int main()
{
  int T;
  int U[2], V[2];

  scanf("%d", &T);
  while(T--)
    {
      scanf("%lld", &n);
      scanf("%s", strC);
      scanf("%d", &M);
      
      processC();
      for(int i = 0; i < M; i++)
	scanf("%d %d", U + i, V + i);
      
      if(M == 0) solve0();
      else if(M == 1) solve1();
      else if(U[0] == V[1] || U[0] == U[1] || V[0] == V[1] || V[0] == U[1])
	solve2_CommonVertex();
      else solve2_DistinctVertex();
      
      calcAns();
    }
  
  return 0;
}
