#include<iostream>
using namespace std;
int main(){
	int a ,b ,p = 1,ans = 0;
	cin>>a>>b;
	
	while(a || b){
		ans += (((b % 3) - (a % 3) + 3) % 3) * p;
		a = a/3;
		b = b/3;
		p = p*3;
	}
	
	cout<<ans<<endl;
	return 0;
}