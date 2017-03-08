#include <bits/stdc++.h>
using namespace std;

int N, i;
string S[50005];

bool c(string a, string b) {return a + b < b + a;}

int main() {
	for (cin >> N; i < N; i++) cin >> S[i];
	for (sort(S, S + N, c), i = 0; i < N; i++) cout << S[i];
}
