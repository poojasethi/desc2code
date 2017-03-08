#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <queue>

#define MAXN 100005

using namespace std;

typedef long long llint;
typedef pair<int, int> pii;

char s[MAXN];

int n, m;

int main(void) {

    scanf("%d%d%s", &n, &m, s);

    llint sol = (llint) n * m - n;
    for (int i = 1; i < n; ++i) 
        sol += (s[i] != s[i - 1]) * ((llint) n * m - n);  

    int curr = 1;
    for (int i = 1; i < n; ++i) {
        if (curr == 1) {
            if (s[i] == s[i - 1]) continue;
            ++curr;
        } else {
            if (s[i] == s[i - 2]) {
                ++curr;
            } else {
                sol -= (llint) curr * (curr - 1) / 2;
                curr = 1 + (s[i] != s[i - 1]);;
            }

        }
    }

    sol -= (llint) curr * (curr - 1) / 2;
    printf("%lld\n", sol);

    return 0;

}

