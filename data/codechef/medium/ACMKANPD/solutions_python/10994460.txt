#include<iostream>
#include<string>
#include<algorithm>
#include<cstdlib>

using std::cin;
using std::cout;
using std::string;
using std::count;
using std::generate;
using std::strtol;

int main() {
	string token;
	string number;
	char flag;
	while (token != "~" and token != "#~") {
		cin >> token;
		if (token == "#" or token == "#~") {
			cout << strtol(number.c_str(), nullptr, 2) << '\n';
			number = "";
		}
		else if (token == "0") {
			flag = '1';
		}
		else if (token == "00") {
			flag = '0';
		}
		else {
			int num_zeros = count(token.begin(), token.end(), '0');
			if (num_zeros == token.size()) {
				string bits(num_zeros - 2, '-');
				generate(bits.begin(), bits.end(), [flag]() { return flag; });
				number += bits;
			}
		}
	}
	return 0;
}