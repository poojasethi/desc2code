#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
using namespace std;

struct state {
	int cost;
	int pos;
	int prev;
	int ramp;
	state(int cost, int pos, int prev, int ramp) : cost(cost), pos(pos), prev(prev), ramp(ramp) {}
	bool operator<(const state& b) const {
		return cost > b.cost;
	}
};

struct edge {
	int next;
	int cost;
	int ramp;
	edge(int next, int cost, int ramp) : next(next), cost(cost), ramp(ramp) {}
	bool operator<(const edge& b) const {
		if (next < b.next) return true;
		if (next > b.next) return false;
		if (cost < b.cost) return true;
		if (cost > b.cost) return false;
		if (ramp < b.ramp) return true;
		if (ramp > b.ramp) return false;
		return false;
	}
};

int main() {
	int n, L; cin >> n >> L;
	map<int, vector<edge> > linked;
	set<int> nodes;
	nodes.insert(0); nodes.insert(L);
	for (int i = 0; i < n; i++) {
		int x, d, t, p; cin >> x >> d >> t >> p;
		linked[x-p].push_back(edge(x+d, p+t, i+1));
		nodes.insert(x-p);
		nodes.insert(x+d);
	}
	vector<int> vnodes;
	for (set<int>::iterator it = nodes.begin(); it != nodes.end(); ++it) {
		vnodes.push_back(*it);
	}
	for (int i = 1; i < vnodes.size(); i++) {
		int x = vnodes[i-1];
		int y = vnodes[i];
		linked[x].push_back(edge(y, y - x, -1));
		linked[y].push_back(edge(x, y - x, -1));
	}

	map<int,int> backs, ramps;
	priority_queue<state> Q;
	state init(0, 0, -1, -1);
	Q.push(init);

	while(!Q.empty()) {
		state top = Q.top(); Q.pop();
		int pos = top.pos;
		int cost = top.cost;
		int prev = top.prev;
		int ramp = top.ramp;
		if (pos < 0) {
			continue;
		}
		if (backs.count(pos))
			continue;
		
		backs[pos] = prev;
		ramps[pos] = ramp;
		if (pos == L) {
			cout << cost << endl;
			break;
		}
		vector<edge>& edges = linked[pos];
		for (int i = 0; i < edges.size(); i++) {
			edge& e = edges[i];
			Q.push(state(cost + e.cost, e.next, pos, e.ramp));
		}
	}

	vector<int> ans;
	int p = L;
	while (p != 0) {
		if (ramps[p] > 0)
			ans.push_back(ramps[p]);
		p = backs[p];
	}
	reverse(ans.begin(), ans.end());

	cout << ans.size() << endl;

	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << " ";
	}
	cout << endl;

	return 0;
}
