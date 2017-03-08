#include <iostream>
#include <map>
using namespace std;

int main() {
	long long a;
	string s;
	cin >> a >> s;

	map<int, long long> count;
	for (int i = 0; i < s.length(); i++) {
		int sum = 0;
		for (int j = i; j < s.length(); j++) {
			sum += s[j] - '0';
			count[sum]++;
		}
	}

	long long ans = 0;
	if (a == 0) {
		ans = count[0] * s.length() * (s.length() + 1) - count[0] * count[0];
	} else {
		for (long long i = 1; i * i <= a; i++) {
			if (a % i == 0) {
				ans += count[i] * count[a/i] * (i * i == a ? 1 : 2);
			}
		}
	}

	cout << ans << endl;

}
