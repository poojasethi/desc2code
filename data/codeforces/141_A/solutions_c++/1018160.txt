#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	string a, b, c, ab;
	cin >> a >> b >> c;
	ab = a+b;
	sort(ab.begin(), ab.end());
	sort(c.begin(), c.end());
	cout << ((ab == c)? "YES":"NO");
}
