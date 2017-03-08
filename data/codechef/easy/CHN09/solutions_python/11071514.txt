#include <iostream>
#include<cstdio>
#include <string>
#include <map>
#include <cstring>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
using namespace std;

int main(){
	int t;
	string s;
	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> s;
		int c = 0;
		for (int j = 0; j < s.size(); j++){
			if (s[j] == 'a') c++;
		}
		if (s.size() - c < c) c = s.size() - c;
		cout << c << endl;
	}
}