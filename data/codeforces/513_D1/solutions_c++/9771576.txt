#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> L[1000009];
vector<int> R[1000009];

int left[1000009];
int right[1000009];

bool ok = true;

int T = 0;
void DFS(int v, int N)
{
    T++;

    sort(L[v].begin(), L[v].end());
    sort(R[v].begin(), R[v].end());

    if (L[v].size()) {
        left[v] = v+1;
        DFS(v+1, L[v].back());
    }

    if (!ok || (R[v].size() && T >= R[v][0])) {
        ok = false;
        return;
    }

    if (N > T || R[v].size()) {
        right[v] = T+1;
        DFS(T+1, max((R[v].size() ? R[v].back() : 0), N));
    }

}

void Print(int v) {
    if (left[v]) Print(left[v]);
    printf("%d ", v);
    if (right[v]) Print(right[v]);
}

int main()
{
    char s[100];
    int n, c; scanf("%d %d", &n, &c);

    while (c--) {
        int a, b;
        scanf("%d%d%s", &a, &b, s);
        if (a >= b) {
            printf("IMPOSSIBLE");
            return 0;
        }
        if (s[0] == 'R')
            R[a].push_back(b);
        else
            L[a].push_back(b);
    }

    DFS(1, n);

    if (ok) {
        Print(1);
    }
    else {
        printf("IMPOSSIBLE");
    }
}
