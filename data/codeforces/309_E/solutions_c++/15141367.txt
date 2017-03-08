#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cctype>
#include<algorithm>

using namespace std;

const int MaxN = 2000 + 5;

int N;
int lside[MaxN], rside[MaxN], ans[MaxN], border[MaxN], sum[MaxN];
bool inter[MaxN][MaxN], valid[MaxN], used[MaxN];

bool check(int dis) {
    memset(valid, true, sizeof(valid));
    memset(used, false, sizeof(used));
    for (int i = 0; i < N; ++i) border[i] = N - 1;
    for (int pos = 0; pos < N; ++pos) {
        int minrpos = -1;
        for (int i = 0; i < N; ++i) if (valid[i])
            if (minrpos == -1 || rside[i] < rside[minrpos])
                minrpos = i;
        if (minrpos == -1) return false;
        ans[pos] = minrpos;
        border[minrpos] = pos;
        used[minrpos] = true;
        for (int i = 0; i < N; ++i) if (inter[i][minrpos])
            border[i] = min(border[i], pos + dis);
        memset(sum, 0, sizeof(sum));
        for (int i = 0; i < N; ++i) sum[border[i]]++;
        for (int i = 1; i < N; ++i) sum[i] += sum[i - 1];
        for (int i = 0; i < N; ++i) if (sum[i] > i + 1) return false;
        int tmp;
        for (int i = pos + 1; i < N; ++i) if (sum[i] == i + 1) {
            tmp = i; break;
        }
        for (int i = 0; i < N; ++i) 
            valid[i] = (!used[i] && border[i] <= tmp);
        
    }
    return true;
}

int main() {

    memset(inter, false, sizeof(inter)); 
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
        scanf("%d%d", lside + i, rside + i);
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            if (rside[i] >= lside[j] && rside[j] >= lside[i])
                inter[i][j] = true;
    int lo = 0, hi = N - 1, mid;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (check(mid)) hi = mid;
        else lo = mid + 1;
    }
    check(lo);
    for (int i = 0; i + 1 < N; ++i) printf("%d ", ans[i] + 1);
    printf("%d\n", ans[N - 1] + 1);

}
