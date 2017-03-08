#include <iostream>
using namespace std;
int main()
{
	int n, k, d, i, j, v[1000];
	long long x=1;	
	cin>>n>>k>>d;
	for (i=0; i<d && x<n; i++) x*=k;
	if (x<n) cout<<-1<<endl;
	else {
		for (i=0; i<n; i++) v[i]=i;
		for (i=0; i<d; i++) {
			for (j=0; j<n; j++) {
				cout<<v[j]%k+1<<" ";
				v[j]/=k;
			}
			cout<<endl;
		}
	}
	return 0;
}
