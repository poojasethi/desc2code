// C. Help Caretaker
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>

using namespace std;

#define MAXN    10

int n, m;
char a[MAXN][MAXN], ans[MAXN][MAXN];
int best = 0;

char P[4][4][4] = {
    {"###",
     ".#.",
     ".#."},
    {".#.",
     ".#.",
     "###"},
    {"..#",
     "###",
     "..#"},
    {"#..",
     "###",
     "#.."}
};

void solve(int x, int y, char c)
{
    if (x >= n - 2) {
        if (c > best) {
            best = c;
            memcpy(ans, a, sizeof(a));
        }
        return;
    }
    if (y >= m - 2) {
        solve(x + 1, 0, c);
        return;
    }

    if (((n - x) * m - 3 * y) / 5 + c <= best) return;

    solve(x, y + 1, c);

    for (int k = 0; k < 4; k++) {
        bool yes = true;
        for (int i = 0; yes && i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (a[x + i][y + j] != '.' && P[k][i][j] != '.') {
                    yes = false;
                    break;
                }
        if (yes) {
            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    if (P[k][i][j] != '.') a[x + i][y + j] = c;

            solve(x, y + 1, c + 1);

            for (int i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    if (P[k][i][j] != '.') a[x + i][y + j] = '.';
        }
    }
}

int main(int argc, char *argv[])
{
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) a[i][j] = '.';

    solve(0, 0, 'A');

    cout << best - 'A' << endl;
    for (int i = 0; i < n; i++) cout << ans[i] << endl;

    return 0;
}