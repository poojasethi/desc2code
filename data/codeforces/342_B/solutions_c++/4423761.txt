#include <iostream>
#include <cstdio>
using namespace std;

int ar[100010][3];

int main(){
	int n,m,s,f,st=0,nowm=0;
	scanf("%d%d%d%d",&n,&m,&s,&f);
	for(int i=0; i<m; ++i)
		scanf("%d%d%d",&ar[i][0],&ar[i][1],&ar[i][2]);
	while(++st){
		if(s==f) break;
		int Catch=false;
		if(ar[nowm][0]==st){
			if(ar[nowm][1]<=s && ar[nowm][2]>=s) Catch=true;
			else if(f>s && ar[nowm][1]==s+1) Catch=true;
			else if(f<s && ar[nowm][2]==s-1) Catch=true;
			++nowm;
		}
		if(Catch) printf("X");
		else{
			if(f>s){ printf("R"); ++s;}
			else{ printf("L"); --s;}
		}
	}
	printf("\n");
	return 0;
}

