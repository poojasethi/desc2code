#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

typedef long long int ll;
const ll INF  = 1e18;

ll ew[300006];
bool flag[300006];
ll n,m, src;

ll a[300006], dist[300006];

struct E{
	ll v, w, id; 
	bool operator< (const E &r) const{
		return w> r.w || (w==r.w && ew[id]> ew[r.id]);
	}
};
vector<E> g[300006];

void dijkstra(){
	priority_queue<E> Q;
	for (int i=0;i<=n;i++)
		dist[i] = INF;
	
	dist[src] = 0;
	Q.push((E){src,0,0});
	
	ll cnt= 0, sum = 0;
	while (!Q.empty()){
		E e  = Q.top();
		Q.pop();
		
		if (flag[e.v]) continue;
		if (cnt==n) break;
		flag[e.v] =1;
		ll u= e.v;
		a[cnt] = e.id;
		sum += ew[e.id];
		cnt++;
		
		for(int j=0;j<g[u].size();j++){
			E e2= g[u][j];
			if ( !flag[e2.v] && dist[u]+ g[u][j].w <= dist[e2.v]){
				dist[e2.v] = dist[u]+ e2.w;
				Q.push((E){e2.v,dist[e2.v],e2.id});
			}
		}
	}
	cout << sum << endl;
	for(int i=1;i<n;i++)
		cout << a[i] <<" ";
	cout << endl;
}
int main(){
  
	cin >> n >> m;

	for (int i=1;i<=m;i++){
		int a,b,c;
		cin >> a >> b >> c;
		g[a].push_back((E){b,c,i}); 
		g[b].push_back((E){a,c,i}); 
		ew[i] = c;
	}
	cin >> src;
	
	dijkstra();
	
	
	return 0;
}
