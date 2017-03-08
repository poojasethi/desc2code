#include <bits/stdc++.h>
#define hash ajsidjaodiajidajsdo
using namespace std;

int n, m;
int a[100005];
int b[100005];
map<int, int> h;

int main() {
    cin >> n;
    int bad = 0;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    for (int i = 0; i < n; i++) {
        h[a[i]]++, h[b[i]]++;
        if (a[i] == b[i]) bad++;
    }
    cin >> m;
    long long ans = 1;
    for (map<int, int>::iterator it = h.begin(); it != h.end(); ++it) {
        for (int i = 1; i <= it->second; i++) {
            int j = i;
            while (bad && j % 2 == 0) j /= 2, bad--;
            ans = (ans * j) % m;
        }
    }
    cout << ans << endl;
    return 0;
}
