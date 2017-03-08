#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;

const int N = 11;

int n;
int mat[N][N];

int leia (int i) {
    scanf("%d", &mat[i/n][i%n]);
    return ((i == (n*n)-1) || leia(i+1));
}

int floyd (int i, int j, int k) {
    mat[i][j] = min(mat[i][k] + mat[k][j], mat[i][j]);
    
    return (
        (k == n-1 && j == n-1 && i == n-1) || 
        ( (j == n-1 && i == n-1)  && floyd(0, 0, k+1) ) ||
        ( (i == n-1) && floyd(0, j+1, k) ) ||
        ( floyd(i+1, j, k) )
    );
}

int imprime (int i) {
    return (i?max(imprime(i-1), mat[i/n][i%n]):0);
}

int main () {
    scanf("%d", &n);

    leia(0);
    floyd(0, 0, 0);
    printf("%d\n", imprime((n*n)-1));
}
