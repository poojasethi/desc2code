#include<iostream>
#include<vector>
#include<queue>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define INF 1000000000

int main(){
	int n,m;
	cin>>n>>m;
	vector<vii> adj;
	adj.assign(n,vii());
	for(int i=0;i<m;i++){
		int x,y;
		cin>>x>>y;
		x--; y--;
		adj[x].push_back(ii(y,0));
		adj[y].push_back(ii(x,1));
	}	

	vi dist(n,INF);
	dist[0]=0;
	priority_queue< ii,vector<ii>,greater<ii> > q;
	q.push(ii(0,0));
	while(!q.empty()){
		ii front =q.top();
		q.pop();
		if(front.first==dist[front.second]){
			for(int i=0;i<(int)adj[front.second].size();i++){
				ii v = adj[front.second][i];
				if(dist[front.second]+v.second<dist[v.first]){
					dist[v.first]=dist[front.second]+v.second;
					q.push(ii(dist[v.first],v.first));
				}
			}
		}
	}
	if(dist[n-1]==INF) cout<<"-1\n";
	else cout<<dist[n-1];
	return 0;
}
