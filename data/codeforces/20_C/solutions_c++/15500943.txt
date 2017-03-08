#include <bits/stdc++.h>
using namespace std;
#define ll long long 
const ll inf = 1LL * 1e9 * 1e9 + 10;
ll m,n,prev[100001],d[100001];
vector<pair<ll ,ll> > edges[100001];
void path(ll i){
	if(i==1){
		cout<<"1";
		return;
	}
	path(prev[i]);
	cout<<" "<<i;
}
int main(){
	ios_base::sync_with_stdio(false);cin.tie(0);
	ll a,b,w;
	cin>>n>>m;
	while(m--){
		cin>>a>>b>>w;
		edges[a].push_back(make_pair(b,w));
		edges[b].push_back(make_pair(a,w));
	}
	set<pair<ll ,ll> > pset;
	for(int i=1;i<=n;i++){
		prev[i]=-1;d[i]=inf;
	}
	d[1]=0;
	pset.insert(make_pair(0,1));
	while(!pset.empty()){
		ll u=pset.begin()->second;
		pset.erase(make_pair(d[u],u));
		ll l=edges[u].size();
		for(int i=0;i<l;i++){
			ll v=edges[u][i].first;
			if(d[v]>d[u]+edges[u][i].second){
				pset.erase(make_pair(d[v],v));
				d[v]=d[u]+edges[u][i].second;
				prev[v]=u;
				pset.insert(make_pair(d[v],v));
			}
		}
	}
	if(prev[n]==-1)cout<<"-1\n";
	else path(n);
	return 0;
}
