#include<bits/stdc++.h>

using namespace std;

int id[1234567],c[1234567];

int main(){
	int n,tp,st=-1,en=-1,rep=0;
	cin >> n;
	for(int i=0;i<n;i++){
		scanf("%d",&tp);
		if(!c[tp]){
			c[tp]=1;
			id[tp]=i;
		}
		else ++c[tp];
		if(c[tp]>rep){
			rep=c[tp];	
			st=id[tp];
			en=i;
		}
		else if(c[tp]==rep && en-st>i-id[tp]){
			st=id[tp];
			en=i;
		}
	}
	cout << st+1 << ' ' << en+1 << endl;
}
