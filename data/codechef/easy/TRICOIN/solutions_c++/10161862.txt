#include <bits/stdc++.h>
using namespace std;

long long int solve(long long int n) {
	 long long int determinant = 1 + 8*n;

	  long long x = (-1 + sqrt(determinant))/2;
	  return x;
}

int main(int argc, char const *argv[])
{
	long long int tc;
	cin>>tc;
	while(tc--) {
		long long int n;
		cin>>n;

		cout << solve(n) << "\n";
	} 
	return 0;
}
