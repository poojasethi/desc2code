#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>
using namespace std;
const int SHIFT = 100000000;
long long fuck(string s) {
    int n = s.length();
    long long cpcnt = 0, flag = 0;
    long long crt = 0, tot = 0;
    for (int i = 0; i < n; ++i) {
        char ch = (tot&1)?'R':'L';
        if ('X' == s[i]) {
            ++tot;
        } else if (ch == s[i]) {
            ++tot, ++crt, flag = 0;
        } else {
            tot += 2;
            ++crt;
            cpcnt += flag;
            flag = !flag;
        }
    }
    if (tot&1) {
        ++tot;
        cpcnt += flag;
    }
    if (crt*2 > tot) {
        crt -= cpcnt;
        tot -= 2*cpcnt;
    }
    return crt*SHIFT/tot;
}
const int MAXN = 1000005;
const int SHIFT2 = 1000000;
char t[MAXN];
int main() {
    gets(t);
    string s;
    s += t[0];
    for (int i = 1; t[i]; ++i) {
        if (t[i] != 'X' && t[i] == t[i-1])
            s += 'X';
        s += t[i];
    }
    long long ans = 0;
    if (s[0] != 'X' && s[0] == s[s.size()-1]) {
        ans = max(fuck('X'+s),fuck(s+'X'));
    } else {
        ans = fuck(s);
    }

    printf("%I64d.%06I64d\n", ans/SHIFT2, ans%SHIFT2);
    return 0;
}
