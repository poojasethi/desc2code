#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int n,m,i,j,a[101][101],f=0;
	cin>>n>>m;
	for(i=0;i<n;i++)
	for(j=0;j<m;j++)
		cin>>a[i][j];	
	while(n%2==0) {
		f=0;
		for (i=0; i<n/2&&f==0; i++) 
			for (j=0; j<m&&f==0; j++)
				if (a[i][j]!=a[n-i-1][j]) f=1;
		if (f==0) n/=2;
		else break; 
	}
	cout<<n;
	return 0;	
}