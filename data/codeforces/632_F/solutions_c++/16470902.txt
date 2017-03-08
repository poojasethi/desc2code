#include<bits/stdc++.h>

#define MAX 2501

using namespace std;

int mat[MAX][MAX];
int p[MAX];
int dis[MAX];

vector<int> ady[MAX];

int n;

bitset<MAX> v;

int Find(int x){
	if(p[x] == x)return x;
	return p[x] = Find(p[x]);
}

void Union(int x, int y){
	x = Find(x);
	y = Find(y);
	if(x == y)return;
	p[x] = y;
	ady[x].push_back(y);
	ady[y].push_back(x);
}

struct Edge{
	int x, y, c;
	Edge(){}
	Edge(int _x, int _y, int _c){x = _x; y = _y; c = _c;}
};

bool cmp(Edge a, Edge b){
	return a.c < b.c;
}

vector<Edge> ar;

void dfs(int x, int d){
	v[x] = 1;
	dis[x] = d;
	int sz = ady[x].size(), y;
	for(int i = 0 ; i < sz ; ++i){
		y = ady[x][i];
		if(v[y] == 0)dfs(y, max(d, mat[x][y]));
	}
}

int main(){
	scanf("%d", &n);
	for(int i = 0 ; i < n; ++i){
		for(int j = 0 ; j < n ; ++j){
			scanf("%d", &mat[i][j]);
		}
	}
	
	for(int i = 0 ; i < n; ++i){
		for(int j = i ; j < n ; ++j){
			if(i == j){
				if(mat[i][j] != 0){
					printf("NOT MAGIC\n");
					exit(0);
				}
			}
			else{
				if(mat[i][j] != mat[j][i]){
					printf("NOT MAGIC\n");
					exit(0);
				}
			}
		}
	}
	
	for(int i = 0 ; i < n ; ++i){
		for(int j = i+1 ; j < n; ++j){
			ar.push_back(Edge(i, j, mat[i][j]));
		}
	}
	
	for(int i = 0 ; i < MAX ; ++i)p[i] = i;
	
	int sz = ar.size();
	
	int x, y;
	
	sort(ar.begin(), ar.end(), cmp);
	
	for(int i = 0 ; i < sz ; ++i){
		x = ar[i].x;
		y = ar[i].y;
		
		if(Find(x) == Find(y))continue;
		Union(x, y);
	}
	
	for(int i = 0 ; i < n ; ++i){
		v.reset();
		dfs(i, 0);
		for(int j = 0 ; j < n ; ++j){
			if(dis[j] !=  mat[i][j]){
				
				printf("NOT MAGIC\n");
				exit(0);
			}
		}
	}
	
	printf("MAGIC\n");
	
	return 0;
}
