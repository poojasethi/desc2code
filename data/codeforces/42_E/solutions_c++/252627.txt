/*
 * E. Baldman and the military.cpp
 *
 *  Created on: 2011-1-15
 *      Author: wjmzbmr
 */
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();e++)
using namespace std;
const int MAX_VERTEX=100000+10;
typedef long long int64;
struct EdgeData{
	int s,t,c;
	EdgeData(int _s,int _t,int _c):
		s(_s),t(_t),c(_c){}
	bool operator<(const EdgeData&edgeData) const{
		return c<edgeData.c;
	}
};
struct Edge{
	int t,c;
	Edge(int _t,int _c):
		t(_t),c(_c){}
};
vector<Edge> adj[MAX_VERTEX];
vector<EdgeData> edges;
void addEdge(int s,int t,int c){
	adj[s].push_back(Edge(t,c));
	adj[t].push_back(Edge(s,c));
}
int nVets;
void inputGraph(){
	int nEdges;
	scanf("%d",&nVets);
	scanf("%d",&nEdges);
	int s,t,c;
	for(int e=0;e<nEdges;e++){
		scanf("%d%d%d",&s,&t,&c);
		--s;--t;
		edges.push_back(EdgeData(s,t,c));
	}
}

struct UF{
	int F[MAX_VERTEX];
	void makeUse(int n){
		for(int i=0;i<n;i++)
			F[i]=i;
	}
	int find(int x){
		if(x==F[x])return x;
		return F[x]=find(F[x]);
	}
	bool Union(int a,int b){
		a=find(a);b=find(b);
		F[a]=b;return a!=b;
	}
};

int treeCnt;
int64 treeCost;

UF U;
void calcMST(){
	U.makeUse(nVets);
	sort(edges.begin(),edges.end());

	treeCnt=nVets;treeCost=0;
	foreach(e,edges){
		if(U.Union(e->s,e->t)){
			treeCnt--;
			treeCost+=e->c;
			addEdge(e->s,e->t,e->c);
		}
	}
}

const int MAX_LOG=18;
int que[MAX_VERTEX];
int dep[MAX_VERTEX];

int anc[MAX_VERTEX][MAX_LOG],maxCost[MAX_VERTEX][MAX_LOG];
int root;

void prepare(){
	root=0;
	int h=0,t=0;
	memset(anc,-1,sizeof anc);
	que[t++]=root;dep[root]=0;
	for(;h<t;h++){
		int u=que[h];
		foreach(e,adj[u])
			if(e->t!=anc[u][0]){
				dep[e->t]=dep[u]+1;
				anc[e->t][0]=u;
				maxCost[e->t][0]=e->c;
				que[t++]=e->t;
				for(int log=0;;log++){
					int itsAnc=anc[e->t][log];
					if(itsAnc==-1)break;
					anc[e->t][log+1]=anc[itsAnc][log];
					maxCost[e->t][log+1]=max(maxCost[e->t][log],maxCost[itsAnc][log]);
				}
			}
	}
}

int getMaxCost(int u,int v){
	if(dep[u]<dep[v])
		swap(u,v);

	int res=0;
	#define update(x) if(x>res)res=x;
	for(int log=MAX_LOG-1;log>=0;log--)
		if(dep[u]-(1<<log)>=dep[v]){
			update(maxCost[u][log]);
			u=anc[u][log];
		}
	if(u==v) return res;
	for(int log=MAX_LOG-1;log>=0;log--){
		int au=anc[u][log],av=anc[v][log];
		if(au==av)continue;
		update(maxCost[u][log]);
		update(maxCost[v][log]);
		u=au;v=av;
	}
	update(maxCost[u][0]);
	update(maxCost[v][0]);
	return res;
	#undef update
}

void solve(){
	calcMST();
	int nQuerys;
	scanf("%d",&nQuerys);
	if(treeCnt>2){
		for(int i=0;i<nQuerys;i++)
			puts("-1");
		return;
	} else if(treeCnt==2){
		for(int i=0;i<nQuerys;i++){
			int a,b;scanf("%d%d",&a,&b);
			--a;--b;
			if(U.find(a)!=U.find(b))
				printf("%I64d\n",treeCost);
			else
				puts("-1");
		}
	} else {
		prepare();
		for(int i=0;i<nQuerys;i++){
			int a,b;scanf("%d%d",&a,&b);
			--a;--b;
			printf("%I64d\n",treeCost-getMaxCost(a,b));
		}
	}
}

int main(){
	inputGraph();
	solve();
}
