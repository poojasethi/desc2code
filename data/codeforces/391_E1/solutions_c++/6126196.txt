/* Orginal code
 http://codeforces.com/contest/391/submission/6100922

 too lazy to code gain
 */

#include<algorithm>
#include<iostream>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<climits>
#include<fstream>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<cmath>
#include<map>
#include<set>
using namespace std;

#define pb push_back
#define mp make_pair
#define Y second
#define X first

#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)

const double pi     =   acos(-1.0);
const double eps    =   1e-8;



vector <string> parse(string s, string c)
{
  int len = c.length(), p = -len, np;
  vector <string> ans;

  do
    {
      np = s.find(c, p+len);
      ans.push_back(s.substr(p+len, np - p - len));
      p = np;
    }
  while (p != string::npos);

  return ans;
}

/*Solution code starts here */


typedef long long ll;
using namespace std;

ll Ans, Res, Tmp, S[4][1005], ST[4], MaxS[4];
int N[4], D[4][1005], P[4][1005][12];
vector<int> E[1005];

void dfs(int n, int p, int t, int d)
{
    D[t][n] = d;
    P[t][n][0] = p;

      for(int i=0;i<E[n].size();i++)
      {
           int v=E[n][i];

        if(v != p)
            dfs(v, n, t, d+1);

      }
}

int lca(int t, int u, int v)
{
    if(D[t][u] < D[t][v])
        swap(u,v);

    for(int i = 0; i < 12; i++)
        if((D[t][u] - D[t][v]) & (1 << i))
            u = P[t][u][i];

    if(u == v)
        return u;

    for(int i = 11; i >= 0; i--)
        if(P[t][u][i] != P[t][v][i])
            u = P[t][u][i], v = P[t][v][i];

    return P[t][u][0];
}

int dist(int t, int u, int v)
{
    int l = lca(t, u, v);
    return D[t][u] + D[t][v] - 2*D[t][l];
}

int main()
{
    cin >> N[1] >> N[2] >> N[3];
    Ans = N[1] * N[2] + N[2] * N[3];

    for(int t = 1; t <= 3; t++)
    {
        for(int i = 1; i <= N[t]; i++)
            E[i].clear();

        for(int i = 1; i < N[t]; i++)
        {
            int a, b;
            cin >> a >> b;
            E[a].push_back(b), E[b].push_back(a);
        }

        dfs(1, 0, t, 0);

        for(int l = 1; l < 12; l++)
            for(int n = 1; n <= N[t]; n++)
                P[t][n][l] = P[t][ P[t][n][l-1] ][l-1];

        for(int u = 1; u <= N[t]; u++)
        {
            for(int v = 1; v <= N[t]; v++)
                S[t][u] += dist(t, u, v);

            ST[t] += S[t][u];
            MaxS[t] = max(MaxS[t], S[t][u]);
        }

        ST[t] /= 2;
    }

    for(int d = 1; d <= 3; d++)
    {
        Res = ST[1] + ST[2] + ST[3];

        for(int t = 1; t <= 3; t++)
            if(t != d)
                Res += MaxS[t] * (N[1] + N[2] + N[3] - N[t]) + N[t] * N[d];

        Tmp = 0;

        int t1 = d == 1 ? 2 : 1;
        int t2 = d == 3 ? 2 : 3;

        for(int u = 1; u <= N[d]; u++)
            for(int v = 1; v <= N[d]; v++)
                Tmp = max(Tmp, (ll) (N[t1] * S[d][u] + N[t2] * S[d][v] + N[t1] * N[t2] * (dist(d,u,v) + 2)));

        Ans = max(Ans, Res + Tmp);
    }

    cout << Ans;

    return 0;
}
