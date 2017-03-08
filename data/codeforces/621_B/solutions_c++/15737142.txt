#include <bits/stdc++.h>
using namespace std;

int n, x, y, ans;
map<int, int> cont[2];

int main () {
    scanf ("%d", &n);
    ans = 0;
    for (int i = 0; i < n; i++) {
        scanf ("%d %d", &x, &y);
        ans += cont[0][x-y]+cont[1][x+y];
        cont[0][x-y]++;
        cont[1][x+y]++;
    }
    cout << ans << endl;
}
