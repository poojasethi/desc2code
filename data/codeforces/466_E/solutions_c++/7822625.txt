/*************************************************************************
    > File Name: E.cpp
    > Author: Stomach_ache
    > Mail: sudaweitong@gmail.com
    > Created Time: 2014年09月13日 星期六 01时11分16秒
    > Propose: 
 ************************************************************************/
#include <set>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <fstream>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
/*Let's fight!!!*/

const int MAX_N = 100050;
int n, m, t, x, y;
int G[MAX_N];
int start[MAX_N], end[MAX_N], fa[MAX_N];
#define rep(i, n) for (int i = (0); i < (n); i++)

int findfa(int x) {
  	return x != fa[x] ? fa[x] = findfa(fa[x]) : x;
}

int main(void) {
  	ios::sync_with_stdio(false);
	cin >> n >> m;
	for (int i = 1; i <= n; i++) fa[i] = i;
	int cnt = 1;
	rep (i, m) {
	  	cin >> t;
		if (t == 1) {
		  	cin >> x >> y;
			fa[x] = y;
			G[x] = y;
		} else if (t == 2) {
		  	cin >> x;
			start[cnt] = x;
			end[cnt++] = findfa(x);
		} else {
		  	cin >> x >> y;
			bool flag = false;
			int u = start[y];
			while (true) {
				if (u == x) {
				  	flag = true;
					break;
				}
				if (u == end[y]) break;
				u = G[u];
			}
			if (flag) cout << "YES\n";
			else cout << "NO\n";
		}
	}

	return 0;
}
