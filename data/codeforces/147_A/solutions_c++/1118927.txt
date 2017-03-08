#include <string>
#include <iostream>
using namespace std;
int isP(int c){
	return c=='.'||c==','||c=='!'||c=='?';
}
int main(){
	string s,t,u;
	getline(cin,s);
	for(int i=0;i<s.size();i++){
		if(s[i]==' '||isP(s[i])){
			string x=" ";
			while(i<s.size()&&(s[i]==' '||isP(s[i]))){
				if(isP(s[i]))
					x=s[i],x+=' ';
				i++;
			}
			i--;
			t+=x;
		}else{
			t+=s[i];
		}
	}
	cout<<t<<endl;
	return 0;
}

