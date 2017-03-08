#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>

#define foreach(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++ i)

const int N = 100000 + 10;
const int M = N << 1;

std::map<int, int> children[M];
int prev[M], step[M];
int node_count, last;

void clear(int u) {
    children[u].clear();
    prev[u] = step[u] = 0;
}

void copy_data(int to, int from) {
    children[to] = children[from];
    prev[to] = prev[from];
    step[to] = step[from];
}

void initialise() {
    node_count = 1;
    last = 1;
    clear(1);
}

int insert(int key, int last) {
    int u = ++ node_count, node;
    clear(u);
    step[u] = step[last] + 1;
    for (node = last; node && children[node][key] == 0; node = prev[node]) {
        children[node][key] = u;
    }
    if (node == 0) {
        prev[u] = 1;
    } else {
        int v = children[node][key];
        if (step[v] == step[node] + 1) {
            prev[u] = v;
        } else {
            int nv = ++ node_count;
            copy_data(nv, v);
            step[nv] = step[node] + 1;
            prev[u] = prev[v] = nv;
            for (; node && children[node][key] == v; node = prev[node]) {
                children[node][key] = nv;
            }
        }
    }
    return u;
}

std::vector<int> neighbors[N];
int n;

void dfs(int u, int p, int last) {
    int new_last = insert(neighbors[u].size(), last);
    foreach(iter, neighbors[u]) {
        int v = *iter;
        if (v != p) {
            dfs(v, u, new_last);
        }
    }
}

int main() {
    scanf("%d", &n);
    for (int i = 1; i < n; ++ i) {
        int u, v;
        scanf("%d%d", &u, &v);
        neighbors[u].push_back(v);
        neighbors[v].push_back(u);
    }
    initialise();
    dfs(1, 0, 1);
    long long answer = 0;
    for (int i = 1; i <= node_count; ++ i) {
        answer += step[i] - step[prev[i]];
    } 
    std::cout << answer << std::endl;
    return 0;
}
