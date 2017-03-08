#include <bits/stdc++.h>

using namespace std;

int n, a, b, m = 0;
vector<int> t[1111111];
int ma[1111111], mi[1111111];

void nodem(int r);
void nodeM(int r) {
    if (t[r].empty()) {ma[r] = mi[r] = 0; m++; return;}
    ma[r] = 11111111; mi[r] = t[r].size() - 1;
    for (int i = 0; i<t[r].size(); i++) { nodem(t[r][i]); ma[r] = min(ma[r], ma[t[r][i]]); mi[r] += mi[t[r][i]]; }
}
void nodem(int r) {
    if (t[r].empty()) {ma[r] = mi[r] = 0; m++; return;}
    ma[r] = t[r].size() - 1; mi[r] = 11111111;
    for (int i = 0; i<t[r].size(); i++) { nodeM(t[r][i]); ma[r] += ma[t[r][i]]; mi[r] = min(mi[r], mi[t[r][i]]); }
}

int main() {

    scanf("%d", &n);

    for (int i=0;i<n-1;i++) {scanf(" %d %d", &a, &b); t[a].push_back(b);}

    nodeM(1);

    printf("%d %d\n", m - ma[1], mi[1] + 1);

    return 0;
}
