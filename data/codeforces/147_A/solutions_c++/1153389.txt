#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

string s;

int main() {
	getline(cin, s);
	int n = s.size();
	for (int i = 0; i < n; i++) {
		if (isalpha(s[i])) cout << s[i];
		else if (s[i] == ' ') {
			if (i < n - 1 && isalpha(s[i + 1]))
				cout << s[i];
		}
		else {
			cout << s[i];
			if (i < n - 1 && isalpha(s[i + 1]))
				cout << " ";
		}
	}
	cout << endl;
	return 0;
}
