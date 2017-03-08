/**
 * Description:
 * ProblemName:
 * Source:
 * Author: Ply_py
 */
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <stack>
using namespace std;

const int MAXN = 1e6+5;
int lmin[MAXN], lmax[MAXN], rmin[MAXN], rmax[MAXN];
int n, c;
int pos = 0;
int ans[MAXN];
int ct;
bool flag = true;

void dfs(int largest)
{
    int u = ++pos;
    // lchild
    if (n+1 != lmin[u]) { // not empty
        if (lmin[u] <= pos) {
            flag = false;
            return;
        }
        dfs(lmax[u]);
        if (!flag) {
            return;
        }
    }

    ans[ct++] = u; // root
    // rchild
    if (n+1 != rmin[u]) {
        if (rmin[u] <= pos) {
            flag = false;
            return;
        }
        dfs(max(rmax[u], largest));
    } else if (pos < largest) {
        dfs(largest);
    }
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin >> n >> c;
    for (int i = 1; i <= n; ++i) {
        lmin[i] = rmin[i] = n+1;
        lmax[i] = rmax[i] = 0;
    }
    for (int i = 0; i < c; ++i) {
        int a, b;
        char str[20];
        cin >> a >> b >> str;
        if ('L' == str[0]) {
            lmin[a] = min(lmin[a], b);
            lmax[a] = max(lmax[a], b);
        } else {
            rmin[a] = min(rmin[a], b);
            rmax[a] = max(rmax[a], b);
        }
    }
    dfs(n);
    if (!flag) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans[0];
        for (int i = 1; i < n; ++i) {
            cout << ' ' << ans[i];
        }
        cout << endl;
    }
    return 0;
}
