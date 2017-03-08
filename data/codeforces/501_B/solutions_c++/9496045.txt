#include <bits/stdc++.h>
using namespace std;

const int MAXN = 3004;

int main(){
	ios_base::sync_with_stdio(0);
	map<string, int> M;
	set<string> us;
	string s, z, A[MAXN], B[MAXN];
	int n, i, it = 0;
	cin >> n;
	for(i = 0; i < n; i++){
		cin >> s >> z;
		if(M.find(s) == M.end()){
			M[s] = it;
			A[it] = s;
			it++;
		}
		B[M[s]] = z;
		M[z] = M[s];		
	}
	cout << it << endl;
	for(i = 0; i <= it; i++){
		cout << A[i] << " " << B[i] << endl;
	}
}
