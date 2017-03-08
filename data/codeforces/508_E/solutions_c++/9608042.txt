#include <bits/stdc++.h>
using namespace std;

#define F first.first
#define S first.second
#define T second

typedef pair< pair<int,int>,int > iii;
	
int main() {
	ios_base::sync_with_stdio(0);
	int n, i, l, r;
	iii aux;
	stack<iii> st;
	string s="";
	cin >> n;
	for(i = 0; i < n; i++){
		cin >> l >> r;
		aux.F = s.size(); aux.S = l; aux.T = r;
		st.push(aux);
		s+='(';
		while(!st.empty() && st.top().F + st.top().S <= s.size()){
			if(st.top().F + st.top().T < s.size()){
				cout << "IMPOSSIBLE\n";
				return 0;
			}
			s += ')';
			st.pop();
		}
	}
	if(!st.empty()) cout << "IMPOSSIBLE\n";
	else 			cout << s << endl;
}
