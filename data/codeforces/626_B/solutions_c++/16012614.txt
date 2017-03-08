#include <bits/stdc++.h>

using namespace std;

int main(){
	int len;
	cin >> len;
	string s;
	cin >> s;
	int tg=0,tb=0,tr=0;
	for (int i=0;i<len;++i)
		if (s[i]=='G')
			++tg;
		else if (s[i]=='B')
			++tb;
		else
			++tr;
	if ((tb==0 && tr>0 && tg>0) || (tb>0 && tr+tg>1) || (tr==0 && tg==0))
		cout << "B";
	if ((tg==0 && tr>0 && tb>0) || (tg>0 && tr+tb>1) || (tr==0 && tb==0))
		cout << "G";
	if ((tr==0 && tb>0 && tg>0) || (tr>0 && tb+tg>1) || (tb==0 && tg==0))
		cout << "R";
}