#include <iostream>
#include <string>
using namespace std;
int main(){
	string s;
	int n,ans=0;
	cin>>s;
	n=s.size();
	for(int i=0;i<n;){
		int v=0,j;
		for(j=i;j<n&&s[i]==s[j];j++)
			;
		v=j-i;
		i=j;
		ans+=(v+5-1)/5;
	}
	cout<<ans<<endl;
	return 0;
}

