#include <bits/stdc++.h>
using namespace std;
int a[3][2]; char A,B,C;
void print1(int h1, int w1, int h2, int w2, int h3, int w3){
	for(int i=0;i<h1;i++){
		for(int j=0;j<w1;j++) cout << A;
		cout << "\n";
	}
	for(int i=0;i<h2;i++){
		for(int j=0;j<w2;j++) cout << B;
		cout << "\n";
	}
	for(int i=0;i<h3;i++){
		for(int j=0;j<w3;j++) cout << C;
		cout << "\n";
	}
}
void print2(int h1, int w1, int h2, int w2, int h3, int w3){
	for(int i=0;i<h1;i++){
		for(int j=0;j<w1;j++) cout << A;
		cout << "\n";
	}
	for(int i=0;i<h2;i++){
		for(int j=0;j<w2;j++) cout << B;
		for(int j=0;j<w3;j++) cout << C;
		cout << "\n";
	}
}
int main(){
	for(int i=0;i<3;i++)
		for(int j=0;j<2;j++)
			cin >> a[i][j];
	for(int i=0;i<3;i++){
		for(int j=0;j<2;j++){
			int f = (i+1)%3, s = (i+2)%3;
			A = 'A' + i, B = 'A' + (i+1)%3, C = 'A' + (i+2)%3; 
			for(int x=0;x<2;x++){
				for(int y=0;y<2;y++){
					if(a[i][j] == a[i][j^1] + a[f][x^1] + a[s][y^1] && a[i][j] == a[f][x] && a[i][j] == a[s][y]){
						cout << a[i][j] << "\n";
						print1(a[i][j^1],a[i][j],a[f][x^1],a[f][x],a[s][y^1],a[s][y]);
						return 0;
					} else if(a[i][j] == a[i][j^1] + a[f][x] && a[f][x] == a[s][y] && a[i][j] == a[f][x^1] + a[s][y^1]){
						cout << a[i][j] << "\n";
 						print2(a[i][j^1],a[i][j],a[f][x],a[f][x^1],a[s][y],a[s][y^1]);
						return 0;
					}
				}
			}
		}
	}
	cout << -1;
}