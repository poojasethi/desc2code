#include <iostream>
#include <string>
using namespace std;

int used[256];
int a[30];

int main(){
	int n; string s;
	cin >> n >> s;
	
	int k= 0;
	for(int i=0; s[i] && k<n; i++)
		if (!used[s[i]]){
			used[s[i]]= 1;
			a[k++] = i;
		}
		
	a[n]= s.length();
	if (k== n){
		cout << "YES" << endl;
		for (int i=0;i<n;i++)	
			cout << s.substr(a[i], a[i+1]- a[i]) << endl;
	}
	else
		cout << "NO" << endl;
	
	return 0;
}
