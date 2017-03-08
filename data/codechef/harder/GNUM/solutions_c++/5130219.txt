#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

struct Edge {
  int from, to, cap, flow, index;
  Edge(int from, int to, int cap, int flow, int index) :
    from(from), to(to), cap(cap), flow(flow), index(index) {}
};

struct PushRelabel {
  int N;
  vector<vector<Edge> > G;
  vector<LL> excess;
  vector<int> dist, active, count;
  queue<int> Q;

  PushRelabel(int N) : N(N), G(N), excess(N), dist(N), active(N), count(2*N) {}

  void AddEdge(int from, int to, int cap) {
    G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
    if (from == to) G[from].back().index++;
    G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
  }

  void Enqueue(int v) { 
    if (!active[v] && excess[v] > 0) { active[v] = true; Q.push(v); } 
  }

  void Push(Edge &e) {
    int amt = int(min(excess[e.from], LL(e.cap - e.flow)));
    if (dist[e.from] <= dist[e.to] || amt == 0) return;
    e.flow += amt;
    G[e.to][e.index].flow -= amt;
    excess[e.to] += amt;    
    excess[e.from] -= amt;
    Enqueue(e.to);
  }
  
  void Gap(int k) {
    for (int v = 0; v < N; v++) {
      if (dist[v] < k) continue;
      count[dist[v]]--;
      dist[v] = max(dist[v], N+1);
      count[dist[v]]++;
      Enqueue(v);
    }
  }

  void Relabel(int v) {
    count[dist[v]]--;
    dist[v] = 2*N;
    for (int i = 0; i < G[v].size(); i++) 
      if (G[v][i].cap - G[v][i].flow > 0)
	dist[v] = min(dist[v], dist[G[v][i].to] + 1);
    count[dist[v]]++;
    Enqueue(v);
  }

  void Discharge(int v) {
    for (int i = 0; excess[v] > 0 && i < G[v].size(); i++) Push(G[v][i]);
    if (excess[v] > 0) {
      if (count[dist[v]] == 1) 
	Gap(dist[v]); 
      else
	Relabel(v);
    }
  }

  LL GetMaxFlow(int s, int t) {
    count[0] = N-1;
    count[N] = 1;
    dist[s] = N;
    active[s] = active[t] = true;
    for (int i = 0; i < G[s].size(); i++) {
      excess[s] += G[s][i].cap;
      Push(G[s][i]);
    }
    
    while (!Q.empty()) {
      int v = Q.front();
      Q.pop();
      active[v] = false;
      Discharge(v);
    }
    
    LL totflow = 0;
    for (int i = 0; i < G[s].size(); i++) totflow += G[s][i].flow;
    return totflow;
  }
};


typedef vector<int> vi;

int gcd(int a, int b){ return b == 0 ? a : gcd(b, a%b);}

vi vA;
map<int,int> gL, gR;
int t, n;



int main(){
  ios_base::sync_with_stdio(false);
  
  cin >> t;
  while(t--){
    cin >> n;
    gL.clear(); gR.clear();
    vA.clear();
    int x;
    for(int i = 0; i < n; i++){
      cin >> x;
      vA.push_back(x);
    }
    int g;
    for(int j = 0; j < n; j++){
      cin >> x;
      
      for(int i = 0; i < n; i++){
        if(vA[i] < x){ // Left
          g = gcd(vA[i],x);
          if(g > 1){
            if(!gL.count(g)){
              gL[g] = 0;
            }
            gL[g]++;
          }
        }
        else if(vA[i] > x){ // Right
          g = gcd(vA[i],x);
          if(g > 1){
            if(!gR.count(g)){
              gR[g] = 0;
            }
            gR[g]++;
          }
        }
      }
    }
    
    int source = 0, target = gL.size()+gR.size() + 1;
    
    PushRelabel df(gL.size() + gR.size() + 2);
    map<int,int>::const_iterator it, it2;
    int id, id2;
    for(it = gL.begin(), id = 1; it != gL.end(); ++it, id++){
      df.AddEdge(source, id, it->second);
    }
    for(it = gR.begin(), id = gL.size()+1;it != gR.end(); ++it, id++){
      df.AddEdge(id, target, it->second);
    }
    
    for(it = gL.begin(), id = 1; it != gL.end(); ++it, id++){
      for(it2 = gR.begin(), id2 = gL.size()+1;it2 != gR.end(); ++it2, id2++){
        if(gcd(it->first, it2->first) > 1){
          df.AddEdge(id,id2, it->second);
        }
      }
    }
    
    cout << df.GetMaxFlow(source, target) << '\n';
    
  }
}
