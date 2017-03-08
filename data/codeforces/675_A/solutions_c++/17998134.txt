#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    if (c == 0) puts(a==b?"YES":"NO");
    else puts(((b-a)%c == 0 && (b-a)/c >= 0)?"YES":"NO");

    return 0;
}
