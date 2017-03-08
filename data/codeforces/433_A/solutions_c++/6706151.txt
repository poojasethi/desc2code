#include <iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	int num100=0;
	for(int i=0; i<n; i++){
		int temp;
		cin>>temp;
		if(temp==100)
			num100++;
	}
	if(n==1 || num100%2!=0 ||(num100==0 && n%2!=0))
		cout<<"NO";
	else 
		cout<<"YES";
	cout<<endl;
}