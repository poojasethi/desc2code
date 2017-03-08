#include <stdio.h>

int rev(int a) {
    int r = 0;
    while (a) {
        r = r*10 + a%10;
        a /= 10;
    }
    return r;
}

const int N = 1000000;
int pt[N];

int main() {
    for (int i = 2; i < N; i++) if (pt[i] == 0) {
        for (int j = i+i; j < N; j+=i) pt[j] = i;
    }
    int n;
    scanf("%d", &n);
    for (int i = 2; i < N; i++) if (pt[i] == 0) {
        if (rev(i) != i && pt[rev(i)] == 0) {
            if (--n == 0) {
                printf("%d\n", i);
                break;
            }
        }
    }
    return 0;
}
