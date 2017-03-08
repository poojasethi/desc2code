#include <bits/stdc++.h>
using namespace std;

const int MAX = 1e5+2;

int main(){
	int n, a[MAX];

	scanf("%d", &n);
	for(int i = 0; i < n; i++) scanf("%d", a+i);

	set<int> s;
	set<int>::iterator it;
	for(int i = 0; i < n; i++){
		s.insert(a[i]);
		it = s.find(a[i]);
		it++;
		if(it != s.end()) s.erase(it);
	}
	printf("%d\n", s.size());
}
