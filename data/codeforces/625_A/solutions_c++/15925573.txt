#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n, a, b, c;
    cin >> n >> a >> b >> c;

    long long a1 = n/a;
    long long a2 = max(0LL, (n - c)/(b - c));
    a2 += (n - a2*(b-c))/a;

    cout << max(a1, a2) << endl;
}
