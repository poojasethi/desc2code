#include <string>
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int n;
int ca[600][600];
int np[600][600];
int pa[600][600];
string s;
int rec(int p,int l){
	if(l<0)				return 10000;
	if(ca[p][l]!=-1)	return ca[p][l];
	if(p==n)			return ca[p][l]=0;
	ca[p][l]=10000;
	for(int pp=p;pp<n;pp++){
		int a=pa[p][pp]+rec(pp+1,l-1);
		if(a<ca[p][l]){
			ca[p][l]=a;
			np[p][l]=pp;
		}
	}
	return ca[p][l];
}
int main(){
	int li;
	cin>>s>>li;
	n=s.size();
	for(int i=0;i<n;i++)
		for(int j=i;j<n;j++){
			int a=0;
			for(int k=i,l=j;k<l;k++,l--)
				if(s[k]!=s[l])
					a++;
			pa[i][j]=a;
		}
	memset(ca,-1,sizeof(ca));
	int v=rec(0,li);
	cout<<v<<endl;
	int pp=0,ll=li,b=1;
	while(1){
		if(!b)	cout<<"+";
		b=0;
		//cout<<pp<<"-"<<np[pp][ll]<<" ";
		string t=s.substr(pp,np[pp][ll]-pp+1);
		int m=t.size();
		for(int i=0,j=m-1;i<j;i++,j--)
			t[j]=t[i];
		cout<<t;
		pp=np[pp][ll]+1;
		ll--;
		if(pp==n)	break;
	}
	cout<<endl;
	return 0;
}

