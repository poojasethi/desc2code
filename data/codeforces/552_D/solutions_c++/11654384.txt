#include <bits/stdc++.h>

using namespace std;

int x[2000], y[2000];
int main() {

    int n;
    scanf("%d", &n);
    for(int i=0; i<n; ++i) scanf("%d %d", &x[i], &y[i]);

    long long tri = 1ll*n*(n-1)*(n-2)/6;

    for(int i=0; i<n; ++i) for(int j=i+1; j<n; ++j) for(int k=j+1; k<n; ++k)
        if ((y[j]-y[i])*(x[k]-x[i])==(y[k]-y[i])*(x[j]-x[i])) --tri;

    printf("%lld\n", tri);

    return 0;
}
