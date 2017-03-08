#include <iostream>
using namespace std;

int main() {
	int A, B, C;
	cin >> A >> B >> C;
	if ((C == 0 && B == A) || (C != 0 && (B-A)%C == 0 && (B-A)/C >= 0))
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
}