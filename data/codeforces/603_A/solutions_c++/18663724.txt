#include<bits/stdc++.h>

using namespace std;

string s;

int main(){

	int n;
	cin>>n;
	int i;

	cin>>s;

	int net=1;
	for(i=0;i<n-1;i++){
		if(s[i]!=s[i+1]){
			net++;
		}

	}

	net=min(net+2,n);
	cout<<net<<endl;



	return 0;
}