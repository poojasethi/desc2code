#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int main() {
	int n;
	while(cin >> n){
		set<int> S;
		char c;
		int x, gg = 0;
		while(n--){
			cin >> c >> x;
			if(c == '+') S.insert(x);
			else{
				if(S.count(x)) S.erase(x);
				else gg++;
			}
			gg = max(gg,(int)S.size());
		}
		cout << gg << endl;
	}
	return 0;
}