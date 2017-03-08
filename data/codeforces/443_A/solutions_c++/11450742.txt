#include<bits/stdc++.h>

using namespace std;

int main(){
	set<char> a;
	char c;
	int ans=0;
	while((c=getchar())!='\n')
		if('a'<=c && c<='z')
			a.insert(c);
	cout << a.size() << endl;
	return 0;
}
