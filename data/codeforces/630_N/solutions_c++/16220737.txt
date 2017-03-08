#include <bits/stdc++.h>

using namespace std;

#define int long double

int32_t main(){
	int a,b,c;
	cin >> a >> b >> c;
	int delta=sqrt(b*b-4*a*c);
	int x1=(delta-b)/(2*a);
	int x2=-(delta+b)/(2*a);
	cout << setprecision(15) << max(x1,x2) << endl << min(x1,x2);
}