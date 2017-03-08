#include<iostream>
#include<fstream>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	char B='B',G='G';
	int x,y;
	cin>>x>>y;
	if(y>x) swap(x,y),swap(B,G);
	while(x|y){
		if(x) cout<<B,x--;
		if(y) cout<<G,y--;
	}
	return 0;
}