#include<bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

#define INF 1000000000

int N, M;
vector<int> edge0[100000], edge1[100000];
 
int dist[100000], visited[100000];
int q[300000], q_st, q_size;
 
int main(){
  int i, j, k;

  scanf("%d%d",&N,&M);
  while(M--){
    scanf("%d%d",&i,&j);
    i--; j--;
    edge0[i].push_back(j); // edge with cost 0 (i -> j)
    edge1[j].push_back(i); // edge with cost 1 (j -> i)
  }
 
  rep(i,N) dist[i] = INF, visited[i] = 0;
  dist[0] = 0;
  
  q_st = 150000; q_size = 0;
  q[q_st+q_size++] = 0;      // deque using ordinary array
 
  while(q_size){ // 01-BFS
    k = q[q_st++]; q_size--;
    if(visited[k]++) continue;
    rep(i,edge0[k].size()){
      j = edge0[k][i];
      if(dist[j] > dist[k]){
        dist[j] = dist[k];
        q[--q_st] = j; q_size++;
      }
    }
    rep(i,edge1[k].size()){
      j = edge1[k][i];
      if(dist[j] > dist[k]+1){
        dist[j] = dist[k]+1;
        q[q_st+q_size++] = j;
      }
    }
  }
 
  if(dist[N-1]==INF) dist[N-1] = -1;
  printf("%d\n",dist[N-1]);
 
  return 0;
}
 