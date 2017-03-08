#include <bits/stdc++.h>

using namespace std;

vector <int> a,b;

int main(){
	int n;
	cin >> n;
	int ind1,ind2;
	for (int i=0;i<n;++i){
		int x;
		cin >> x;
		if (x==1)
			ind1=a.size();
		if (x)
			a.push_back(x);
	}
	for (int i=0;i<n;++i){
		int x;
		cin >> x;
		if (x==1)
			ind2=b.size();
		if (x)
			b.push_back(x);
	}
	for (int i=0;i<n-1;++i)
		if (a[(ind1+i)%(n-1)]!=b[(ind2+i)%(n-1)]){
			cout << "NO";
			return 0;
		}
	cout << "YES";
}