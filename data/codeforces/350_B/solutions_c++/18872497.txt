//resort codeforces - div2

#include <bits/stdc++.h>
using namespace std;

int qnt;
int l[100009], t[100009], s[100009], fin[100009];
int used[100009];

void f(int i){
	
	l[qnt++] = i;
	
	
	if(used[s[i]] > 1 || s[i] == 0)
		return;
	
	else{
		f(s[i]);
		used[s[i]]++;
	}
}


int main() {
	
	int n, i, m, g;
	cin >> n;
	
	for(i = 1; i <= n; i++){
		cin >> t[i];
	}

	for(i = 1; i <= n; i++){
		cin >> s[i];
		
		used[s[i]]++;
	}
	
	g = 0;
	
	for(i = 1; i <= n; i++){
		
		if(t[i] == 1){
			qnt = 0;
			f(i);
			
			if(qnt > g){
				g = qnt;
				
				for(m = 0; m < qnt; m++){
					fin[m] = l[m];
				}
			}
		}
	}
	
	cout << g << endl;
	
	for(i = g - 1; i > -1; i--)
		cout << fin[i] << ' ';
	
	cout << endl;
	return 0;
}
