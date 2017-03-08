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
const int OO = 0x3f3f3f;
//REMEMBER LONG LONG INT
//REMEMBER TO INITIALZE THINGS
int ca[1000007], cb[1000007], cc[1000007];
int main(){
    std::ios::sync_with_stdio(false);
    int n, k;
    cin >> n >> k;
    vector<string> v;
    string aux = "";
    char c;
    for (int i = 1; i <= n; i++) {
        cin >> c;
        aux += c;
        if (i % k == 0) {
            v.pb(aux);
            aux = "";
        }
    }
    for (int i = 0; i < v.size (); i++) {
        for (int j = 0; j < k; j++) {
            if (v[i][j] != 'a') ca[j]++;
            if (v[i][j] != 'b') cb[j]++;
            if (v[i][j] != 'c') cc[j]++;
        }
    }
    char code[] = {'a', 'b', 'c'};
    for (int i = 0; i < k; i++) {
        int mini = INT_MAX, minii;
        if (ca[i] < mini) {
            mini = ca[i];
            minii = 0;
        }
        if (cb[i] < mini) {
            mini = cb[i];
            minii = 1;
        }
        if (cc[i] < mini) {
            mini = cc[i];
            minii = 2;
        }
        cout << code[minii];
    }
    cout << "\n";
}
