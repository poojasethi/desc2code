#include<bits/stdc++.h>
#define g getchar_unlocked
#define ll long long int
using namespace std;
int readnum() {
    int n = 0;
    char c = g();
    while(c < '0' || c > '9') c = g();
    while(c >= '0' && c <= '9') n = 10 * n + c - '0', c = g();
    return n;
}
int power(int x, int y, int n) {
    if(y == 0) {
        if(n == 1)
            return 0;
        return 1;
    }
    if(y == 1) {
        return x % n;
    }
    ll tmp = (ll)power(x, y / 2, n);
    if(y&1) {
        return (((tmp * tmp) % n * x) % n) % n;
    }
    return (tmp * tmp) % n;
}

int main() {
    int t, n, x, y;
    t = readnum();
    n = readnum();
    while(t--) {
        x = readnum();
        y = readnum();
        printf("%d\n", power(x, y, n));
    }
    return 0;
}

