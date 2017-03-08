//header macros
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <unordered_map>
#include <list>
#include <string>
#include <cmath>
#include <iomanip>/*cout << setprecision (10) << fixed;*/
//end header macros
//input macros
# define PI 3.141592653589793238462643383279502884L
#define fr(i,a,n) for(i=a;i<n;i++)
#define pb push_back
#define gcd __gcd
//end input macros 
using namespace std;
int main(){
    long long int t;
	cin >> t;
	for(long long int i=1;i<=t;i++)
	{
		long long int n;
		cin >> n;
		vector<long long int> v;
		for(long long int j=0;j<n;j++)
		{
			long long int x;
			cin >> x;
			v.pb(x);
		}
		sort(v.begin(),v.end());
		cout << "Case " << i << ": ";
		cout << v[n-3]+v[n-2]+v[n-1] << endl;
	}
    return 0;
}
