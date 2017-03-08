#include<iostream>
#include<algorithm>
using namespace std;
long long m,a[5],g[5][5],d[5][5],l;
int main(){
	for(int i=0;i<5;i++)a[i]=i;
	for(int i=0;i<5;i++)for(int j=0;j<5;j++)cin>>g[i][j];
	do{
		l=g[a[0]][a[1]]+g[a[1]][a[0]]+g[a[1]][a[2]]+g[a[2]][a[1]]+2*(g[a[2]][a[3]]+g[a[3]][a[2]]+g[a[3]][a[4]]+g[a[4]][a[3]]);
		m=max(l,m);
	}while(next_permutation(a,a+5));
	cout<<m;
}