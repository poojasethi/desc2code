#include <iostream>
using namespace std;
int main(){
	string num;
	cin >> num;
	for (int i = 0; i < num.length(); i++){
		int x = num.at(i) - '0';
		if (x >= 5 && (x != 9 || i != 0)) x = 9 - x;
		cout << x;
	}
	return 0;
}

