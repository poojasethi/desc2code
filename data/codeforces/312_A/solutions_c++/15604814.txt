#include <bits/stdc++.h>
using namespace std;

int main(){

	int n,l;
	string ss;
	cin>>n;
	while(getline(cin,ss)){
		if(ss.empty()) continue;
		l = ss.size();
		if(l<5){
			printf("OMG>.< I don't know!\n");	
		} 
		else{
			if(ss.substr(l-5,l)!="lala." && ss.substr(0,5)=="miao.") printf("Rainbow's\n");
			else if(ss.substr(l-5,l)=="lala." && ss.substr(0,5)!="miao.") printf("Freda's\n");
				else printf("OMG>.< I don't know!\n");	
		}
	}
		
		
	
	return 0;
}
