#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	string a, b;
	cin >> a >> b;
	sort(a.begin(), a.end());
	int pos;
	for(pos = 0; a[pos] == '0' && pos < a.size()-1; pos ++);
	swap(a[0], a[pos]);
	cout << (a == b ? "OK" : "WRONG_ANSWER") << endl;
	return 0;
}
