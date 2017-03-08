#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <cstring>
#define tr(object, it) \
    for(typeof(object.begin()) it = object.begin(); it != object.end(); ++it)
using namespace std;

int main() {
    stringstream ans;
    queue<int> Q;
    bool flag = true;
    vector< vector < pair <int, long long> > > Gr;
    long N, M, K, u, v, val, last;
    long Weight[200010];
    bool visited[200010] = {false};

    cin >> N >> M >> K;
    Gr.resize(N+1);
    for (long i=0; i<M; ++i) {
        cin >> u >> v >> val;
	Gr[u].push_back(make_pair(v,val));
	Gr[v].push_back(make_pair(u,val));
    }

    for (int i=1; i<=N; ++i) {
	if (flag && !visited[i]) {
	    last = i;
	    Weight[i] = 0;
	    Q.push(i);
	    visited[i] = true;
	    while (!Q.empty() && flag) {
		int elem = Q.front();
		Q.pop();
		tr (Gr[elem], it) {
		    if (!visited[(*it).first]) {
			Weight[(*it).first] = Weight[elem]^((*it).second);
			visited[(*it).first] = true;
			Q.push((*it).first);
		    } else if (Weight[(*it).first] != (Weight[elem]^((*it).second))) {
			flag = false;
			break;
		    }
		}
	    }
	}
    }
    if (!flag) {
	cout << "-1" << endl;
    } else {
	memset(visited, 0, sizeof(visited));
	queue<int> Temp;
	swap(Q, Temp);
	Q.push(last); Weight[last] = (K-1); visited[last]= true;
	while (!Q.empty()) {
	    int elem = Q.front(); Q.pop();
	    tr (Gr[elem], it) {
		if (!visited[(*it).first]) {
		    Weight[(*it).first] ^= (K-1);
		    Q.push((*it).first);
		    visited[(*it).first] = true;
		}
	    }
	}
	int i;
	for (i=1; i<N; ++i) {
	    cout << Weight[i] << " ";
	}
	cout << Weight[i] << endl;
    }
    return 0;
}
