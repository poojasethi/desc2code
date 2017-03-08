#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define debug (args...) fprintf (stderr, args)
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

int n, k, tab[1000005][3];
char s[1000005];

int main () {
    scanf ("%d %d %s", &n, &k, s);
    int bloco = n/k ;
    for (int i = 0; i < k; i++) {
        int let, pos;
        for (int j = 0; j < bloco; j++) {
            pos = i + j*k;
            if (s[pos] == 'a') let = 0;
            else if (s[pos] == 'b') let = 1;
            else let = 2;
            tab[i][let]++;    
        } 
        int ma = -1;
        for (int j = 0; j < 3; j++) {
            if (tab[i][j] > ma)
                ma = tab[i][j], let = j;
        }
        printf ("%c", let+'a');
    }
    printf ("\n");
}

