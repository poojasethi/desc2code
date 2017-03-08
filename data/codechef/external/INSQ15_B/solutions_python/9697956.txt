#include <bits/stdc++.h>
/*
#include <iostream>
#include <cstring>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <map>
*/
#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair
#define fst first
#define scd second
#define f(x, let) for(int let=0; let<x; let++)
#define ms(x, v) memset(x, v, sizeof x)
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pair<int, int> > vpi;
typedef set<int> si;
typedef set<int>::iterator sit;
const int MOD = 1000000007;
const int OO = 1000000000;
//REMEMBER LONG LONG INT
//REMEMBER TO INITIALZE THINGS
int t, n, k;
pi v[207];
int mat[207][37][207];
int mat2[207][207];

int costti (int i, int f) {
    int aux = 0;
    if (mat2[i][f] != -1) return mat2[i][f];
    for (int x = i + 1; x < f; x++) {
        int a = abs (v[x].fst - v[i].fst) + v[i].scd;
        int b = abs (v[x].fst - v[f].fst) + v[f].scd;
        aux += min (a, b);
    }
    mat2[i][f] = aux;
    return aux;
}

int pd (int i, int l, int last) {
    if (i > n && l == 0) return costti (last, n+1);
    if (l != 0 && i > n) return OO;
    if (l < 0) return OO;
    if (mat[i][l][last] != -1) return mat[i][l][last];

    mat[i][l][last] = min (costti (last, i) + pd (i+1, l-1, i), pd (i+1, l, last));
    return mat[i][l][last];
}

int main(){
    std::ios::sync_with_stdio(false);
    cin >> t;
    while (t--) {
        ms (mat, -1);
        ms (mat2, -1);
        cin >> n >> k;
        f (n, i) {
            cin >> v[i+1].fst;
        }
        v[0].fst = 0;
        v[n+1].fst = 0;
        f (n, i) {
            cin >> v[i+1].scd;
        }
        v[0].scd = OO;
        v[n+1].scd = OO;
        sort (v+1, v+n+1);

        int ans = pd (1, k, 0);
        cout << ans << "\n";
    }
}
