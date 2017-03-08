#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main(){
	ll n,k;
	double l,v1,v2;
	cin>>n>>l>>v1>>v2>>k;
	int b = (n+k-1)/k;
	double den =(2*(b-1)*v1/(v1+v2)) +1 ;
	double x = l/den;
	double ans = x/v2 + (l-x)/v1;
	cout.precision(9);
	cout<<ans;
	return 0;
}
