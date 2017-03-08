#include <algorithm>
#include <functional>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>

#define MOD_PRIME 1000000007
#define MAX_N 100000

using namespace std;

vector<int> neighbours[MAX_N];
vector<int> new_nodes;
vector<int> cycle_nodes;
bool visited[MAX_N];
bool in_cycle[MAX_N];
int parent[MAX_N];
int enemy[MAX_N];
int cycle[2];
int dp[MAX_N][2];

int skip_whitespace()
{
	int ch;
	while (true) {
		ch = getchar_unlocked();
		if (ch != ' ' && ch != '\n')
			break;
	}
	return ch;
}

template<typename T>
T read_unsigned_integer()
{
	T result = (T) 0;
	int ch = skip_whitespace();
	while (ch >= '0' && ch <= '9') {
		result = 10 * result + (ch - '0');
		ch = getchar_unlocked();
	}
	return result;
}

int addmod(int x, int y)
{
	int sum = x + y;
	if (sum >= MOD_PRIME)
		sum -= MOD_PRIME;
	return sum;
}

int addmod(int x, int y, int z)
{
	return addmod(x, addmod(y, z));
}

int mulmod(int x, int y)
{
	long long prod = x;
	prod *= y;
	return (int) (prod % MOD_PRIME);
}

void dfs(int root)
{
	new_nodes.push_back(root);
	int prev = parent[root];
	visited[root] = 1;
	for (vector<int>::const_iterator it = neighbours[root].begin(); it != neighbours[root].end(); ++it) {
		int node = *it;
		if (visited[node]) {
			if (node != prev && cycle[0] < 0) {
				cycle[0] = node;
				cycle[1] = root;
			}
		} else {
			parent[node] = root;
			dfs(node);
		}
	}
}

void dfs_no_cycle(int root)
{
	visited[root] = 1;
	for (vector<int>::const_iterator it = neighbours[root].begin(); it != neighbours[root].end(); ++it) {
		int node = *it;
		if (!visited[node] && !in_cycle[node]) {
			dfs_no_cycle(node);
			dp[root][1] = mulmod(dp[root][1], dp[node][0]);
			dp[root][0] = mulmod(dp[root][0], addmod(dp[node][0], dp[node][1]));
		}
	}
}

void mark_cycle()
{
	int node = cycle[1];
	if (node > 0) {
		while (node != cycle[0]) {
			in_cycle[node] = true;
			cycle_nodes.push_back(node);
			node = parent[node];
		}
		in_cycle[node] = true;
		cycle_nodes.push_back(node);
	}
}

int solve_problem()
{
	int n;

	n = read_unsigned_integer<int>();

	fill(enemy, enemy + n, -1);
	fill(in_cycle, in_cycle + n, false);
	fill(visited, visited + n, false);
	for (int i = 0; i < n; i++) {
		neighbours[i].clear();
		fill(dp[i], dp[i] + 2, 1);
	}

	for (int i = 0; i < n; i++) {
		int x = read_unsigned_integer<int>();
		--x;
		enemy[i] = x;
		if (enemy[x] != i) {
			neighbours[i].push_back(x);
			neighbours[x].push_back(i);
		}
	}

	int result = 1;
	for (int i = 0; i < n; i++)
		if (!visited[i]) {
			fill(cycle, cycle + 2, -1);
			parent[i] = -1;
			new_nodes.clear();
			dfs(i);

			int cycle_root = cycle[0];
			cycle_nodes.clear();
			mark_cycle();

			for (vector<int>::const_iterator it = new_nodes.begin(); it != new_nodes.end(); ++it)
				visited[*it] = false;

			if (cycle_root >= 0) {
				for (size_t j = 0; j < cycle_nodes.size(); j++)
					dfs_no_cycle(cycle_nodes[j]);
			} else {
				dfs_no_cycle(i);
			}

			if (cycle_root < 0) {
				int term = addmod(dp[i][0], dp[i][1]);
				result = mulmod(result, term);
			} else {
				int fw[2] = { dp[cycle_nodes.front()][0], 0 };
				for (size_t j = 1; j < cycle_nodes.size(); j++) {
					int crt = cycle_nodes[j];
					int tmp[2];
					tmp[0] = mulmod(dp[crt][0], addmod(fw[0], fw[1]));
					tmp[1] = mulmod(dp[crt][1], fw[0]);
					memcpy(fw, tmp, sizeof(tmp));
				}

				int bw[2] = { 0, dp[cycle_nodes.front()][1] };
				for (size_t j = 1; j < cycle_nodes.size(); j++) {
					int crt = cycle_nodes[j];
					int tmp[2];
					tmp[0] = mulmod(dp[crt][0], addmod(bw[0], bw[1]));
					tmp[1] = mulmod(dp[crt][1], bw[0]);
					memcpy(bw, tmp, sizeof(tmp));
				}

				int term = addmod(fw[0], fw[1], bw[0]);
				result = mulmod(result, term);
			}
		}

	printf("%d\n", result);

	return 0;
}

int main()
{
	int num_tests;

	num_tests = read_unsigned_integer<int>();
	for (int i = 0; i < num_tests; i++)
		solve_problem();

	return 0;
}
