// Codeforces #291 D
// R2D2 and Droid Army

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
using namespace std;

const int MAXN = 100002;
const int MAXM = 7;

int N, M, K;
int A[MAXN][MAXM];

int maxv;
int maxd[MAXM];
multiset<int> s[MAXM];

int sum(multiset<int> s[], int n) {
    int res = 0;
    for (int i = 0; i < n; i++)
        res += *s[i].rbegin();
    return res;
}

int main() {
    scanf("%d%d%d", &N, &M, &K);
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            scanf("%d", &A[i][j]);

    int l = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++)
            s[j].insert(A[i][j]);
        while (l <= i && sum(s, M) > K) {
            for (int j = 0; j < M; j++)
                s[j].erase(s[j].find(A[l][j]));
            l++;
        }
        if (i + 1 - l > maxv) {
            maxv = i + 1 - l;
            for (int j = 0; j < M; j++)
                maxd[j] = *s[j].rbegin();
        }
    }

    for (int i = 0; i < M; i++)
        printf("%d%c", maxd[i], i < M - 1 ? ' ' : '\n');

    return 0;
}
