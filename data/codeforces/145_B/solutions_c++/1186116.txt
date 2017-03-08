#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int a1, a2, a3, a4;
int mask;

#define FIRST_SEVEN 2
#define LAST_FOUR 1

int main() {
    scanf("%d%d%d%d", &a1, &a2, &a3, &a4);
    a1 -= a3, a2 -= a3, a4 -= a3;
    if (a4 == 1) mask = FIRST_SEVEN | LAST_FOUR, a1 --, a2 --;
    else if (a4 == 0) {
        if (a1) mask = LAST_FOUR, a1 --;
        else mask = FIRST_SEVEN, a2 --;
    }
    if (a1 < 0 || a2 < 0 || a4 > 1 || a4 < -1) printf("-1\n");
    else {
        if (mask & FIRST_SEVEN) printf("7");
        for ( ; a1 --; printf("4"));
        for ( ; a3 --; printf("47"));
        for ( ; a2 --; printf("7"));
        if (mask & LAST_FOUR) printf("4");
        printf("\n");
    }
    return 0;
}