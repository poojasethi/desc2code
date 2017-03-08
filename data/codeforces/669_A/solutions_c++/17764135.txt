#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	cout << N/3*2+(N%3 != 0) << endl;
}