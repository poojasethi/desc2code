#include<iostream>
#include<algorithm>
#define FOR(i,a,b) for(int i = a; i<b; i++)
using namespace std;
int main ()
{
	int n,a[100010];cin>>n;
	FOR(i,0,n)
		cin>>a[i];
	cout<<a[1]-a[0]<<" "<<a[n-1]-a[0]<<endl;
	FOR(i,1,n-1)
		cout<<min(a[i]-a[i-1],a[i+1]-a[i])<<" "
		<<max(a[i]-a[0],a[n-1]-a[i])<<endl;
	cout<<a[n-1]-a[n-2]<<" "<<a[n-1]-a[0]<<endl;
}
