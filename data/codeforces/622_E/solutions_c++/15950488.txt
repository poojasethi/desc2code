#include<bits/stdc++.h>
#define MAX 500005

using namespace std;

vector<int> ady[MAX];
vector<int> res;

bitset<MAX> v;

void dfs(int x, long long h){
	if(v[x] == 1)return;
	v[x] = 1;
	int sz = ady[x].size();
	if(sz == 1 && x != 1){
		res.push_back(h);
		return;
	}
	for(int i = 0 ; i < sz ; ++i){
		dfs(ady[x][i], h+1);
	}
}

int solve(int x){
	int sz;
	res.clear();
	
	dfs(x, 0);
	
	sort(res.begin(), res.end());
	
	sz = res.size();
	
	for(int i = 1 ; i < sz ; ++i){
		res[i] = max(res[i-1] + 1, res[i]);
	}
	
	return 1 + res[sz-1];
}

int main(){
	int n, x, y;
	cin >> n;
	
	v.reset();
	
	for(int i = 1 ; i < n ; ++i){
		scanf("%d %d", &x, &y);
		ady[x].push_back(y);
		ady[y].push_back(x);
	}
	
	int ans = 0;
	int sz = ady[1].size();
	v[1] = 1;
	for(int i = 0 ; i < sz ; ++i){
		ans = max(solve(ady[1][i]), ans);
	}
	
	cout << ans << endl;
}
