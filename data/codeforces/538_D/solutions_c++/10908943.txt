#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    char board[50][50], moves[100][100];

    scanf("%d", &n);

    for (int j=0; j < n; j++) for (int i =0; i<n; i++)
        scanf(" %c", &board[i][j]);

    for (int j=0; j < 100; j++) for (int i =0; i<100;i++)
        moves[i][j] = 'x';
    moves[n-1][n-1] = 'o';

    for (int j=0; j < n; j++) for (int i =0; i<n; i++) if (board[i][j] == 'o')
        for(int l=0; l<n; l++) for(int k=0; k<n; k++) if (board[k][l] == '.')
            moves[n-1+(k-i)][n-1+(l-j)]='.';

    for (int j=0; j < n; j++) for (int i =0; i<n; i++) if (board[i][j] == 'x') {
        bool match = false;
        for(int l=0; l<n; l++) for(int k=0; k<n; k++) if (board[k][l] == 'o')
            if (moves[n-1+(i-k)][n-1+(j-l)]=='x') {match = true;}
        if (!match) {printf("NO\n"); return 0;}
    }

    printf("YES\n");
    for (int j=0; j< 2*n-1; j++) {
        for (int i =0 ; i < 2*n-1;i++)
            printf("%c", moves[i][j]);
        printf("\n");
    }
    return 0;
}

