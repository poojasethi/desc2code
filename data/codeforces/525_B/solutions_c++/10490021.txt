#include <bits/stdc++.h>
using namespace std;

int main(){
	string str;
	int n;
	cin >> str >> n;
	vector<int> vec(str.size());
	for(int i = 0 ; i < n ; i++){
		int tmp;
		cin >> tmp;
		vec[tmp-1]++;
	}
	int t = 0;
	for(int i = 0 ; i < str.size() / 2 ; i++){
		t += vec[i];
		t &= 1;
		if( t )
			swap(str[i], str[str.size()-1-i]);
	}
	cout << str << endl;
}
