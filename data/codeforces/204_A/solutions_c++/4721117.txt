#include<iostream>
using namespace std;
long long f(long long n){
	long long aux = n;
	while(aux >= 10) aux /= 10;
	//cout<<aux<<endl;
	if(n < 10) return n;
	else return n/10 + 9 - (n%10 < aux);
}
int main(){
	long long l,r;
	cin>>l>>r;
	cout<<f(r) - f(l - 1)<<endl;
	return 0;
}