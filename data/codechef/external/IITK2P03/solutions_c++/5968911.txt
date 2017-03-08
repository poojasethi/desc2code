#include<bits/stdc++.h>
typedef long long int ll;
using namespace std;
#define N 205
ll mat[N][N];
int Graph[N][N];
bool bfs(int n, int m, int *parent)
{
  bool visited[N];
  memset(visited,0,sizeof(visited));
  queue<int> q;
  q.push(0);
  visited[0] = true;
  parent[0] = -1;
  while(!q.empty())
  {
    int u = q.front();
    q.pop();
    for(int v=0; v<=n+m+1; v++)
    {
      if(!visited[v] && Graph[u][v] >0)
      {
        q.push(v);
        parent[v] = u;
        visited[v] = true;
      }
    }
  }

  return (visited[n+m+1] == true);
}

int ford(int n, int m)
{
  int source = 0;
  int sink = n+m+1;
  int parent[N];
  int max_flow = 0;

  while(bfs(n,m,parent))
  {
    int path_flow = INT_MAX;
    for(int i = sink; i!= source; i = parent[i])
    {
      path_flow = min(path_flow,Graph[parent[i]][i]);
    }
    for(int i = sink; i!=source; i = parent[i])
    {
      int v = parent[i];
      Graph[i][v] += path_flow;
      Graph[v][i] -= path_flow;
    }
    max_flow += path_flow;
  }
  return max_flow;
}

ll binary(int n,int m, int k)
{
  ll low = 1;
  long long high = 1e12;
  while(low<high)
  {
    ll mid = (low+high)/2;
    memset(Graph,0,sizeof(Graph));
    for(int i=1; i<=n; i++)
      Graph[0][i] = 1;
    for(int i=n+1; i<=n+m; i++)
      Graph[i][n+m+1] = 1;
    for(int i=1; i<=n; i++)
      for(int j=1; j<=m; j++)
      {
        if(mat[i][j] <= mid)
          Graph[i][n+j] = 1;
      }
    int done = ford(n,m);
    if(done>=k)
      high = mid;
    else
      low = mid + 1;
  }
  return low;
}

int main()
{
  int n,m,k;
  cin>>n>>m>>k;
  for(int i=1; i<=n;i++)
    for(int j=1; j<=m; j++)
      scanf("%lld",&mat[i][j]);
  cout<<binary(n,m,k)<<endl;
  return 0;
}
