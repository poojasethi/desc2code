#include <bits/stdc++.h>
#define pos first
#define fee second
#define pb push_back
#define mp make_pair
#define debug (args...) fprintf (stderr, args)
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

const int MAX = 205;
const int INF = 1000000007;

int n, k;
int me[MAX][40], me2[MAX][MAX];
pii city[MAX];

int sum (int a, int b, int kind) {
    int acc = 0;
    if (kind == 0) {
        for (int i = a+1; i <= b; i++) 
           acc += city[i].pos - city[a].pos;
        acc += (b-a) * city[a].fee;
    } else {
        for (int i = a; i < b; i++) 
            acc += city[b].pos - city[i].pos;
        acc += (b-a) * city[b].fee;
    }
    return acc;
}

int best (int a, int b) {
    if (me2[a][b] != -1) return me2[a][b];
    int acc = 0;
    for (int i = a+1; i < b; i++) 
        acc += min (city[i].pos - city[a].pos + city[a].fee, city[b].pos - city[i].pos + city[b].fee); 
    return me2[a][b] = acc;
}

int dp (int i, int k) {
    if (k == 0) 
        return sum (i, n-1, 0);    
    if (i == n-1) return INF;
    if (me[i][k] != -1) return me[i][k];
    int ans = INT_MAX;
    for (int j = i+1; j < n; j++) 
        ans = min (ans, best (i, j) + dp (j, k-1)); 
    return me[i][k] = ans;
}

int main () {
    int t;
    scanf ("%d", &t);
    while (t--) {
        memset (me, -1, sizeof me);
        memset (me2, -1, sizeof me2);
        scanf ("%d %d", &n, &k);
        for (int i = 0; i < n; i++) 
            scanf ("%d", &city[i].pos);
        for (int i = 0; i < n; i++) 
            scanf ("%d", &city[i].fee);
        sort (city, city+n);
        int ans = INT_MAX;
        for (int i = 0; i < n; i++) 
            ans = min (ans, sum (0, i, 1) + dp (i, k-1)); 
        printf ("%d\n", ans);
    }
}



