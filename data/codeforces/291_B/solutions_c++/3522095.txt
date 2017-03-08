#include <iostream>
#include <string>

using namespace std;

int main()
{
	string s;
	getline(cin,s);	
	int n=s.length();
	int i=0;
	while(i<n){
		if(s[i]=='"'){
			cout<<"<";
			do{
				i++;
				if(s[i]!='"'){
					cout<<s[i];
				}	
			}while(s[i]!='"');
			i++;
			cout<<">\n";
		}
		else if(s[i]!=' '){
			cout<<"<";
			while(i<n && s[i]!=' ' && s[i]!='"' ){
				cout<<s[i];
				i++;
			}
			cout<<">\n";
		}
		if(s[i]==' ')
			i++;
	}
	return 0;
}
