#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <iostream>
using namespace std;


int R[1000003][2], to_left[1000003], to_right[1000003], L[1000003][2];
vector<int> S;
int N, C;
bool ok;

// build a subtree, rooted at i and contains vertex to
// returns the largest element in the subtree
int build(int i, int to) {
	if(!ok)return -1;
	
	if(!to_right[i] && to_left[i]){
		int m = build(i+1, max(to, L[i][1]));
		S.push_back(i);
		return m;
	}
	if(!to_left[i] && to_right[i]){
		S.push_back(i);
		return build(i+1, max(to,R[i][1]));
	}
	if(!to_left[i] && !to_right[i]) {
		if(i==to){
			S.push_back(i);
			return i;
		}
		S.push_back(i);
		return build(i+1, to);
	}
	if(to_left[i] && to_right[i]){
		int m = build(i+1, L[i][1]);
		if(m>=R[i][0]){
			ok = false;
			return -1;
		}
		S.push_back(i);
		int n = build(m+1, max(R[i][1], to));
		return n;
	}
}

int main(){
	int u,v;
	string type;
	scanf("%d%d",&N,&C);
	for(int i=1;i<=N;++i){
		R[i][0] = N+1;
		L[i][0] = N+1;
		R[i][1] = 0;
		L[i][1] = 0;
	}
	ok = true;
	for(int i=0;i<C;++i){
		scanf("%d%d",&u,&v);
		cin>>type;
		if(v <= u) {
			ok = false;
			break;
		}
		if(type == "RIGHT"){
			R[u][0] = min(R[u][0],v);
			R[u][1] = max(R[u][1],v);
			to_right[u] = 1;
		}
		else {
			L[u][0] = min(L[u][0],v);
			L[u][1] = max(L[u][1],v);
			to_left[u] = 1;
		}
	}
	build(1, N);
	if(ok){
		for(int i=0;i<N;++i){
			if(i!=0)printf(" ");
			printf("%d",S[i]);
		}
		printf("\n");
	} else {
		printf("IMPOSSIBLE\n");
	}
	return 0;
}