#include <stdio.h>
#include <iostream>
using namespace std;
typedef long long Int;

const int a[30] = {
    0,1,2,1,4,3,2,1,5,6,2,1,8,7,5,9,8,7,3,4,7,4,2,1,10,9,3,6,11,12
};
int h[100000];

int main() {
    Int n;
    cin >> n;
    int ans = 0, uv = n;
    for (Int i = 1; i*i <= n; i++) if (h[i] == 0) {
        int cnt = 1;
        if (i > 1) for (Int j = i*i; j <= n; j *= i) {
            cnt++;
            if (j < 100000) h[j] = 1;
        }
        ans ^= a[cnt];
        uv -= cnt;
    }
    if (uv % 2) ans ^= 1;
    puts(ans ? "Vasya" : "Petya");
    return 0;
}
